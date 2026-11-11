# Robô que posta sozinho no Instagram @lindsonalmeida_ (roda no PC do Lindson pelo Agendador de Tarefas a cada 15 min).
# Fila: https://lindsonalmeida.pages.dev/api/agenda-ig (fonte única; o Windsor também consulta). Publica pela API oficial do Instagram (Graph API).
# Tokens: arquivo criptografado (DPAPI, só este usuário do Windows abre) em %LOCALAPPDATA%\RoboInstagram\tokens.xml. Nunca no repositório.
# Uso: robo-instagram.ps1           (publica se estiver na hora)
#      robo-instagram.ps1 -Teste    (só confere tokens, conta e fila; não publica)
param([switch]$Teste)
$ErrorActionPreference = 'Stop'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$Pasta = Join-Path $env:LOCALAPPDATA 'RoboInstagram'
$Api = 'https://lindsonalmeida.pages.dev/api/agenda-ig'
$Graph = 'https://graph.facebook.com/v21.0'
$Log = Join-Path $Pasta 'robo.log'
New-Item -ItemType Directory -Force -Path $Pasta | Out-Null

function Log($m) { $l = '{0:yyyy-MM-dd HH:mm:ss}  {1}' -f (Get-Date), $m; Add-Content -Path $Log -Value $l -Encoding UTF8; Write-Host $l }
function Segredo($s) { [Runtime.InteropServices.Marshal]::PtrToStringBSTR([Runtime.InteropServices.Marshal]::SecureStringToBSTR($s)) }

# Trava local: nunca duas execuções ao mesmo tempo
$Trava = Join-Path $Pasta 'rodando.lock'
if ((Test-Path $Trava) -and ((Get-Date) - (Get-Item $Trava).LastWriteTime).TotalMinutes -lt 40) { Log 'Outra execução em andamento. Saindo.'; exit 0 }
Set-Content $Trava $PID

try {
  $arq = Join-Path $Pasta 'tokens.xml'
  if (-not (Test-Path $arq)) { throw 'Tokens não encontrados. Rode instalar-robo-instagram.ps1 primeiro.' }
  $t = Import-Clixml $arq
  $Meta = Segredo $t.Meta; $Robo = Segredo $t.Robo; $IgUser = $t.IgUser
  $H = @{ Authorization = "Bearer $Robo" }
  $Nome = "robo-pc-$env:COMPUTERNAME"

  function Api-Get { Invoke-RestMethod -Uri "$Api`?proximo" -Headers $H -TimeoutSec 60 }
  function Api-Post($corpo) {
    $b = [Text.Encoding]::UTF8.GetBytes(($corpo | ConvertTo-Json -Compress))
    Invoke-RestMethod -Uri $Api -Method Post -Headers $H -ContentType 'application/json; charset=utf-8' -Body $b -TimeoutSec 60
  }
  function G-Post($caminho, $campos) {
    $campos['access_token'] = $Meta
    $r = Invoke-RestMethod -Uri "$Graph/$caminho" -Method Post -Body $campos -TimeoutSec 120
    if (-not $r.id) { throw "Graph sem id em $caminho" }; $r.id
  }
  function G-Get($caminho, $campos) { Invoke-RestMethod -Uri "$Graph/$caminho`?fields=$campos&access_token=$([uri]::EscapeDataString($Meta))" -TimeoutSec 60 }
  function Espera-Pronto($cont, $minutos) {
    $fim = (Get-Date).AddMinutes($minutos)
    while ((Get-Date) -lt $fim) {
      $s = (G-Get $cont 'status_code,status').status_code
      if ($s -eq 'FINISHED') { return }
      if ($s -eq 'ERROR' -or $s -eq 'EXPIRED') { throw "Contêiner $cont com status $s" }
      Start-Sleep -Seconds 15
    }
    throw "Contêiner $cont não ficou pronto em $minutos min"
  }

  # 1. Conferências
  $conta = G-Get $IgUser 'username'
  Log "Conta Instagram: @$($conta.username)"
  $f = Api-Get
  if (-not $f.post) { Log 'Fila vazia: nada agendado.'; return }
  $p = $f.post
  Log "Próximo: $($p.id) ($($p.formato)) '$($p.titulo)' liberado em $($f.liberado_em) | pode agora: $($f.pode_agora)"
  if ($Teste) { Log 'Modo teste: tudo certo, nada foi publicado.'; return }

  # 2. Hora: só dentro de 8h–21h (relógio do PC, fuso de São Luís) e quando a API liberar. Se faltar até 14 min, espera.
  $h = (Get-Date).Hour
  if ($h -lt 8 -or $h -ge 21) { Log 'Fora da janela 8h–21h. Saindo.'; return }
  $lib = [DateTime]::Parse($f.liberado_em).ToUniversalTime()
  $falta = ($lib - (Get-Date).ToUniversalTime()).TotalSeconds
  if ($falta -gt 14 * 60) { Log ("Ainda não é hora (faltam {0:N0} min)." -f ($falta / 60)); return }
  if ($falta -gt 0) { Log ("Esperando {0:N0} s até a hora do post." -f $falta); Start-Sleep -Seconds ([int]$falta + 5); $f = Api-Get; $p = $f.post }
  if (-not $f.pode_agora) { Log "API ainda não liberou ($($p.id)). Saindo."; return }

  # 3. Trava na API (nunca postar duas vezes; 409 = outro robô/Windsor pegou ou já postado)
  try { Api-Post @{ id = $p.id; acao = 'pegar'; por = $Nome } | Out-Null }
  catch { Log "Não peguei $($p.id): $($_.Exception.Message)"; return }

  try {
    $leg = [string]$p.legenda
    switch ($p.formato) {
      'carrossel' {
        $filhos = foreach ($u in $p.urls) {
          $campos = @{ is_carousel_item = 'true' }
          if ($u -match '\.(mp4|mov)$') { $campos.media_type = 'VIDEO'; $campos.video_url = $u } else { $campos.image_url = $u }
          $c = G-Post "$IgUser/media" $campos; Espera-Pronto $c 10; $c
        }
        $cont = G-Post "$IgUser/media" @{ media_type = 'CAROUSEL'; children = ($filhos -join ','); caption = $leg }
        Espera-Pronto $cont 10
      }
      'reels' {
        $campos = @{ media_type = 'REELS'; video_url = $p.urls[0]; caption = $leg; share_to_feed = 'true' }
        if ($p.capa -and $p.capa -notmatch '\.(mp4|mov)$') { $campos.cover_url = $p.capa }
        $cont = G-Post "$IgUser/media" $campos; Espera-Pronto $cont 20
      }
      default {
        $cont = G-Post "$IgUser/media" @{ image_url = $p.urls[0]; caption = $leg }; Espera-Pronto $cont 5
      }
    }
    $mid = G-Post "$IgUser/media_publish" @{ creation_id = $cont }
    $link = (G-Get $mid 'permalink').permalink
    Log "PUBLICADO $($p.id): $link"
    Api-Post @{ id = $p.id; acao = 'publicado'; media_id = $mid; link = $link; por = $Nome } | Out-Null

    # Stories do post, se existirem (lista de URLs em "stories")
    foreach ($s in @($p.stories)) {
      if (-not $s) { continue }
      try {
        $campos = @{ media_type = 'STORIES' }
        if ($s -match '\.(mp4|mov)$') { $campos.video_url = $s } else { $campos.image_url = $s }
        $c = G-Post "$IgUser/media" $campos; Espera-Pronto $c 10
        $sid = G-Post "$IgUser/media_publish" @{ creation_id = $c }; Log "Story publicado: $sid"
      } catch { Log "Story falhou: $($_.Exception.Message)" }
    }
  } catch {
    $msg = $_.Exception.Message
    if ($_.ErrorDetails.Message) { $msg = "$msg | $($_.ErrorDetails.Message)" }
    $msg = $msg -replace 'access_token=[^&\s"]+', 'access_token=***'
    Log "ERRO ao publicar $($p.id): $msg"
    try { Api-Post @{ id = $p.id; acao = 'erro'; msg = $msg; por = $Nome } | Out-Null } catch {}
  }
} catch {
  Log ("ERRO: " + ($_.Exception.Message -replace 'access_token=[^&\s"]+', 'access_token=***'))
} finally { Remove-Item $Trava -ErrorAction SilentlyContinue }
