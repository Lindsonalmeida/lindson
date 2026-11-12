# Robô SDR: cria o ícone "Robô SDR" na área de trabalho e liga sozinho com o Windows (sem PowerShell no dia a dia)
$pasta = Split-Path -Parent $MyInvocation.MyCommand.Path
$vbs = Join-Path $pasta 'ligar-escondido.vbs'
$sh = New-Object -ComObject WScript.Shell
foreach ($dest in @([Environment]::GetFolderPath('Desktop'), [Environment]::GetFolderPath('Startup'))) {
  Get-ChildItem $dest -Filter 'Rob*SDR*.lnk' -ErrorAction SilentlyContinue | Remove-Item
  $l = $sh.CreateShortcut((Join-Path $dest 'Robô SDR.lnk'))
  $l.TargetPath = 'wscript.exe'; $l.Arguments = '"' + $vbs + '"'; $l.WorkingDirectory = $pasta
  $l.IconLocation = 'C:\Windows\System32\shell32.dll,24'; $l.Save()
}
Write-Host 'Pronto: ícone Robô SDR na área de trabalho e ligando sozinho com o Windows.'
