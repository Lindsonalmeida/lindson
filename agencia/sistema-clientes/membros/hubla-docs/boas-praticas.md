> For the complete documentation index, see [llms.txt](https://hubla.gitbook.io/docs/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://hubla.gitbook.io/docs/webhooks/boas-praticas.md).

# Boas práticas

Recomendamos que você revise as seguintes práticas recomendadas para garantir a segurança e o bom funcionamento dos seus webhooks na integração com a Hubla.

***

## Verificar se eventos são enviados da Hubla

A Hubla envia eventos de webhook apenas a partir de uma lista específica de endereços IP. Portanto, é importante confiar somente em eventos recebidos desses endereços IP.

Além disso, verifique o token do webhook fornecido pela Hubla para confirmar que os eventos recebidos foram realmente enviados pela plataforma. A Hubla assina cada evento enviado aos endpoints incluindo o seu Hubla Token único no cabeçalho **x-hubla-token**, garantindo assim sua autenticidade.

***

## Gerenciar eventos duplicados

Embora o webhook da Hubla seja projetado para minimizar eventos duplicados, pode ocorrer que endpoints de webhook recebam o mesmo evento mais de uma vez. Para proteger-se contra eventos duplicados, é importante tornar o processamento dos eventos idempotente.

Uma abordagem eficaz é registrar os eventos já processados e evitar processá-los novamente. Você pode detectar eventos duplicados de webhook verificando o cabeçalho **x-hubla-idempotency** na requisição do webhook. Esse cabeçalho contém um identificador único para cada evento e permite que você compare-o com registros anteriores para determinar se a solicitação atual representa um evento duplicado.

***

## Ouça apenas os tipos de eventos exigidos pela sua integração

Configure seus endpoints de webhook para receber somente os tipos de eventos exigidos por sua integração. Escutar eventos adicionais (ou todos os eventos) sobrecarrega seu servidor e não é recomendável.

***

## Ordem de eventos <a href="#event-ordering" id="event-ordering"></a>

A Hubla não garante a entrega dos eventos na ordem em que foram gerados. Portanto, seu serviço não deve esperar a entrega desses eventos em uma ordem específica e deve processá-los conforme são recebidos.

Por exemplo, a criação de uma assinatura pode gerar os seguintes eventos:

* `subscription.created`
* `invoice.created`
* `invoice.status_updated` // (status unpaid)
* `invoice.status_updated` // (status paid)
* `invoice.payment_succeeded`
* `subscription.activated`
* `customer.member_added`

Seu serviço não deve depender da entrega desses eventos em uma ordem específica e deve ser capaz de processá-los independentemente da sequência de recebimento.

***

## Gerenciar atrasos

Em circunstâncias raras, pode ocorrer atrasos no recebimento de webhooks. No entanto, na Hubla, as entidades de assinatura (subscription) e fatura (invoice) são sempre enviadas com dados de versão que representam um valor atômico. Além disso, informações como data de criação (createdAt) e data da última modificação (modifiedAt) podem ser utilizadas para confrontar os valores já presentes em seu sistema.

Ao enfrentar atrasos na entrega dos webhooks da Hubla, você pode seguir estas práticas recomendadas:

1. Utilize a propriedade "version" presente nas entidades de assinatura e fatura para garantir que apenas as atualizações mais recentes sejam processadas. Comparando o valor da versão recebida com o valor armazenado previamente em seu sistema, você pode evitar processamentos desnecessários ou conflitos causados por eventos desatualizados.
2. Verifique também os campos "createdAt" e "modifiedAt". Essas informações permitem comparar as datas das entidades recebidas com as datas registradas anteriormente em seus registros. Dessa forma, é possível confirmar se houve alguma modificação relevante desde a última interação com essas entidades.

***

## Gerencie falhas <a href="#track-failures" id="track-failures"></a>

A Hubla disponibiliza um painel de histórico dos eventos enviados. Nesse painel, é possível rastrear quaisquer falhas nas entregas. Utilize os filtros fornecidos para identificar e corrigir quaisquer problemas antes que afetem os usuários.

***

## Gerencie eventos de forma assíncrona

Configure o seu serviço para processar eventos recebidos com uma fila assíncrona. Você pode encontrar problemas de escalabilidade se optar por processar eventos síncronos. Qualquer pico grande em entregas de webhook (por exemplo, quando as assinaturas são renovadas) pode sobrecarregar os hosts do endpoint. As filas assíncronas garante que seu sistema seja resiliente a um alto volume de requisições.

***

## Retornar rapidamente uma resposta 2xx

É importante que o seu endpoint retorne rapidamente um código de status de sucesso (2xx) antes de qualquer lógica complexa que possa levar a um timeout da requisição. Por exemplo, ao atualizar uma fatura do cliente como paga no sistema contábil, é recomendado retornar uma resposta 200 antes de prosseguir com a atualização em si.

***

## Otimize o gerenciamento da conexão

O sistema responsável pela entrega dos webhooks utiliza HTTP Keep-Alive para reutilizar conexões com o mesmo host e endpoint. Isso reduz a congestão na rede e diminui a latência nas solicitações subsequentes. Verifique se você tem o Keep-Alive habilitado no seu endpoint para aproveitar esse recurso e reduzir as sobrecargas ao receber várias solicitações simultâneas.

***

## Receber eventos com um servidor HTTPS

Ao utilizar URLs com HTTPS para o endpoint do webhook, a Hubla valida a segurança da conexão com o servidor antes de enviar dados do webhook. Portanto, certifique-se de configurar corretamente seu servidor para aceitar HTTPS com um certificado válido. É importante observar que os webhooks da Hubla não são compatíveis com TLS v1.3 neste momento.

***

## Serviço de webhook isenta de proteção contra CSRF

Se estiver usando Rails, Django, Laravel ou outra estrutura da web, seu site pode verificar automaticamente se cada solicitação POST contém um token CSRF. Esse é um importante recurso de segurança que ajuda a proteger você e seus usuários contra tentativas de falsificação de solicitações entre sites. No entanto, essa medida de segurança também pode evitar que seu site processe eventos legítimos. Se for o caso, você pode precisar isentar a rota dos webhooks da proteção contra CSRF.

***
