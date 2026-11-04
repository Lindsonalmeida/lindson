> For the complete documentation index, see [llms.txt](https://hubla.gitbook.io/docs/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://hubla.gitbook.io/docs/webhooks/eventos/membro.md).

# Membro

## Eventos

* [Acesso concedido](#acesso-concedido)
* [Acesso removido](#acesso-removido)

***

## Acesso concedido

{% columns %}
{% column width="33.33%" %}

### 💡 O que é

Avisa que uma pessoa passou a ser membro de um produto seu. Junto com o aviso, você recebe os dados dessa pessoa, do produto e da assinatura.
{% endcolumn %}

{% column width="33.33%" %}

### ⚡ Quando dispara

Quando um membro passa a ter acesso a um determinado produto.
{% endcolumn %}

{% column width="33.33%" %}

### 🎯 Por que utilizar

Com esse aviso, você pode liberar o acesso em outras ferramentas ou dar as boas-vindas ao novo membro assim que ele entrar.
{% endcolumn %}
{% endcolumns %}

{% tabs %}
{% tab title="Recorrente" %}

```json
{
  "type": "customer.member_added",
  "event": {
    "product": {
      "id": "inAVzweR0QYw5y03K5mq",
      "name": "Integrações com Webhook 2.0"
    },
    "products": [{
      "id": "inAVzweR0QYw5y03K5mq",
      "name": "Integrações com Webhook 2.0",
      "offers": [{
        "id": "inAVzweR0QYw5y03K5mq",
        "name": "Principal",
        "cohorts": [{ "id": "3a96c85e-cf82-4236-b242-7431f405c521" }]
      }]
    }],
    "subscription": {
      "id": "e144be20-01d8-4fdc-9eb7-5ca255035c4b",
      "sellerId": "O4fgEI93QqYjs3IBdvUeS12JqbA3",
      "payerId": "Yf7Ahs5DOJRTLvFf84s4uOp7B7Q2",
      "type": "recurring",
      "status": "active",
      "billingCycleMonths": 1,
      "credits": 31,
      "paymentMethod": "credit_card",
      "autoRenew": true,
      "freeTrial": false,
      "activatedAt": "2024-03-28T15:46:46.839Z",
      "modifiedAt": "2024-03-28T15:46:47.436Z",
      "createdAt": "2024-03-28T15:46:47.436Z",
      "firstPaymentSession": {
        "ip": "220.172.165.140",
        "utm": {
          "source": "email",
          "medium": "active-campaign",
          "campaign": "[LEAD][QUENTE][24][MAR]",
          "content": "2024032812H",
          "term": "PROMO25OFF"
        }
      },
      "version": 4
    },
    "user": {
      "id": "Yf7Ahs5DOJRTLvFf84s4uOp7B7Q2",
      "firstName": "John",
      "lastName": "Doe",
      "document": "08351973955",
      "email": "john.doe@hub.la",
      "phone": "+5511988646782"
    }
  },
  "version": "2.0.0"
}
```

{% endtab %}

{% tab title="Pagamento Único" %}

```json
{
  "type": "customer.member_added",
  "event": {
    "product": {
      "id": "inAVzweR0QYw5y03K5mq",
      "name": "Integrações com Webhook 2.0"
    },
    "products": [{
      "id": "inAVzweR0QYw5y03K5mq",
      "name": "Integrações com Webhook 2.0",
      "offers": [{
        "id": "inAVzweR0QYw5y03K5mq",
        "name": "Principal",
        "cohorts": [{ "id": "3a96c85e-cf82-4236-b242-7431f405c521" }]
      }]
    }],
    "subscription": {
      "id": "e144be20-01d8-4fdc-9eb7-5ca255035c4b",
      "sellerId": "O4fgEI93QqYjs3IBdvUeS12JqbA3",
      "payerId": "Yf7Ahs5DOJRTLvFf84s4uOp7B7Q2",
      "type": "one_time",
      "status": "active",
      "billingCycleMonths": 1,
      "credits": 31,
      "paymentMethod": "credit_card",
      "autoRenew": true,
      "freeTrial": false,
      "activatedAt": "2024-03-28T15:46:46.839Z",
      "modifiedAt": "2024-03-28T15:46:47.436Z",
      "createdAt": "2024-03-28T15:46:47.436Z",
      "firstPaymentSession": {
        "ip": "220.172.165.140",
        "utm": {
          "source": "email",
          "medium": "active-campaign",
          "campaign": "[LEAD][QUENTE][24][MAR]",
          "content": "2024032812H",
          "term": "PROMO25OFF"
        }
      },
      "version": 4
    },
    "user": {
      "id": "Yf7Ahs5DOJRTLvFf84s4uOp7B7Q2",
      "firstName": "John",
      "lastName": "Doe",
      "document": "08351973955",
      "email": "john.doe@hub.la",
      "phone": "+5511988646782"
    }
  },
  "version": "2.0.0"
}
```

{% endtab %}

{% tab title="Gratuito" %}

```json
{
  "type": "customer.member_added",
  "event": {
    "product": {
      "id": "inAVzweR0QYw5y03K5mq",
      "name": "Integrações com Webhook 2.0"
    },
    "products": [{
      "id": "inAVzweR0QYw5y03K5mq",
      "name": "Integrações com Webhook 2.0",
      "offers": [{
        "id": "inAVzweR0QYw5y03K5mq",
        "name": "Principal",
        "cohorts": [{ "id": "3a96c85e-cf82-4236-b242-7431f405c521" }]
      }]
    }],
    "subscription": {
      "id": "e144be20-01d8-4fdc-9eb7-5ca255035c4b",
      "sellerId": "O4fgEI93QqYjs3IBdvUeS12JqbA3",
      "payerId": "Yf7Ahs5DOJRTLvFf84s4uOp7B7Q2",
      "type": "free",
      "status": "active",
      "billingCycleMonths": 1,
      "credits": 730,
      "autoRenew": true,
      "freeTrial": false,
      "activatedAt": "2024-03-28T15:46:46.839Z",
      "modifiedAt": "2024-03-28T15:46:47.436Z",
      "createdAt": "2024-03-28T15:46:47.436Z",
      "version": 4
    },
    "user": {
      "id": "Yf7Ahs5DOJRTLvFf84s4uOp7B7Q2",
      "firstName": "John",
      "lastName": "Doe",
      "document": "08351973955",
      "email": "john.doe@hub.la",
      "phone": "+5511988646782"
    }
  },
  "version": "2.0.0"
}
```

{% endtab %}

{% tab title="FreeTrial" %}

```json
{
  "type": "customer.member_added",
  "event": {
    "product": {
      "id": "inAVzweR0QYw5y03K5mq",
      "name": "Integrações com Webhook 2.0"
    },
    "products": [{
      "id": "inAVzweR0QYw5y03K5mq",
      "name": "Integrações com Webhook 2.0",
      "offers": [{
        "id": "inAVzweR0QYw5y03K5mq",
        "name": "Principal",
        "cohorts": [{ "id": "3a96c85e-cf82-4236-b242-7431f405c521" }]
      }]
    }],
    "subscription": {
      "id": "e144be20-01d8-4fdc-9eb7-5ca255035c4b",
      "sellerId": "O4fgEI93QqYjs3IBdvUeS12JqbA3",
      "payerId": "Yf7Ahs5DOJRTLvFf84s4uOp7B7Q2",
      "type": "recurring",
      "status": "active",
      "billingCycleMonths": 1,
      "credits": 7,
      "paymentMethod": "credit_card",
      "autoRenew": true,
      "freeTrial": true,
      "activatedAt": "2024-03-28T15:46:46.839Z",
      "modifiedAt": "2024-03-28T15:46:47.436Z",
      "createdAt": "2024-03-28T15:46:47.436Z",
      "firstPaymentSession": {
        "ip": "220.172.165.140",
        "utm": {
          "source": "email",
          "medium": "active-campaign",
          "campaign": "[LEAD][QUENTE][24][MAR]",
          "content": "2024032812H",
          "term": "TRIAL7"
        }
      },
      "version": 4
    },
    "user": {
      "id": "Yf7Ahs5DOJRTLvFf84s4uOp7B7Q2",
      "firstName": "John",
      "lastName": "Doe",
      "document": "08351973955",
      "email": "john.doe@hub.la",
      "phone": "+5511988646782"
    }
  },
  "version": "2.0.0"
}
```

{% endtab %}
{% endtabs %}

***

## Acesso removido

{% columns %}
{% column width="33.33%" %}

### 💡 O que é

Avisa que uma pessoa deixou de ser membro de um produto seu. Junto com o aviso, você recebe os dados dessa pessoa, do produto e da assinatura.
{% endcolumn %}

{% column width="33.33%" %}

### ⚡ Quando dispara

Quando um membro não tem mais acesso a um determinado produto.
{% endcolumn %}

{% column width="33.33%" %}

### 🎯 Por que utilizar

Com esse aviso, você pode remover o acesso em outras ferramentas e manter sua lista de membros sempre atualizada.
{% endcolumn %}
{% endcolumns %}

{% tabs %}
{% tab title="Recorrente" %}

```json
{
  "type": "customer.member_removed",
  "event": {
    "product": {
      "id": "inAVzweR0QYw5y03K5mq",
      "name": "Integrações com Webhook 2.0"
    },
    "products": [{
      "id": "inAVzweR0QYw5y03K5mq",
      "name": "Integrações com Webhook 2.0",
      "offers": [{
        "id": "inAVzweR0QYw5y03K5mq",
        "name": "Principal",
        "cohorts": [{ "id": "3a96c85e-cf82-4236-b242-7431f405c521" }]
      }]
    }],
    "subscription": {
      "id": "e144be20-01d8-4fdc-9eb7-5ca255035c4b",
      "sellerId": "O4fgEI93QqYjs3IBdvUeS12JqbA3",
      "payerId": "Yf7Ahs5DOJRTLvFf84s4uOp7B7Q2",
      "type": "recurring",
      "status": "inactive",
      "billingCycleMonths": 1,
      "credits": 0,
      "paymentMethod": "credit_card",
      "autoRenew": true,
      "freeTrial": false,
      "activatedAt": "2024-03-28T15:46:46.839Z",
      "modifiedAt": "2024-03-28T15:46:47.436Z",
      "createdAt": "2024-03-28T15:46:47.436Z",
      "firstPaymentSession": {
        "ip": "220.172.165.140",
        "utm": {
          "source": "email",
          "medium": "active-campaign",
          "campaign": "[LEAD][QUENTE][24][MAR]",
          "content": "2024032812H",
          "term": "PROMO25OFF"
        }
      },
      "version": 4
    },
    "user": {
      "id": "Yf7Ahs5DOJRTLvFf84s4uOp7B7Q2",
      "firstName": "John",
      "lastName": "Doe",
      "document": "08351973955",
      "email": "john.doe@hub.la",
      "phone": "+5511988646782"
    }
  },
  "version": "2.0.0"
}
```

{% endtab %}

{% tab title="Pagamento Único" %}

```json
{
  "type": "customer.member_removed",
  "event": {
    "product": {
      "id": "inAVzweR0QYw5y03K5mq",
      "name": "Integrações com Webhook 2.0"
    },
    "products": [{
      "id": "inAVzweR0QYw5y03K5mq",
      "name": "Integrações com Webhook 2.0",
      "offers": [{
        "id": "inAVzweR0QYw5y03K5mq",
        "name": "Principal",
        "cohorts": [{ "id": "3a96c85e-cf82-4236-b242-7431f405c521" }]
      }]
    }],
    "subscription": {
      "id": "e144be20-01d8-4fdc-9eb7-5ca255035c4b",
      "sellerId": "O4fgEI93QqYjs3IBdvUeS12JqbA3",
      "payerId": "Yf7Ahs5DOJRTLvFf84s4uOp7B7Q2",
      "type": "one_time",
      "status": "inactive",
      "billingCycleMonths": 1,
      "credits": 0,
      "paymentMethod": "credit_card",
      "autoRenew": true,
      "freeTrial": false,
      "activatedAt": "2024-03-28T15:46:46.839Z",
      "modifiedAt": "2024-03-28T15:46:47.436Z",
      "createdAt": "2024-03-28T15:46:47.436Z",
      "firstPaymentSession": {
        "ip": "220.172.165.140",
        "utm": {
          "source": "email",
          "medium": "active-campaign",
          "campaign": "[LEAD][QUENTE][24][MAR]",
          "content": "2024032812H",
          "term": "PROMO25OFF"
        }
      },
      "version": 4
    },
    "user": {
      "id": "Yf7Ahs5DOJRTLvFf84s4uOp7B7Q2",
      "firstName": "John",
      "lastName": "Doe",
      "document": "08351973955",
      "email": "john.doe@hub.la",
      "phone": "+5511988646782"
    }
  },
  "version": "2.0.0"
}
```

{% endtab %}

{% tab title="Gratuito" %}

```json
{
  "type": "customer.member_removed",
  "event": {
    "product": {
      "id": "inAVzweR0QYw5y03K5mq",
      "name": "Integrações com Webhook 2.0"
    },
    "products": [{
      "id": "inAVzweR0QYw5y03K5mq",
      "name": "Integrações com Webhook 2.0",
      "offers": [{
        "id": "inAVzweR0QYw5y03K5mq",
        "name": "Principal",
        "cohorts": [{ "id": "3a96c85e-cf82-4236-b242-7431f405c521" }]
      }]
    }],
    "subscription": {
      "id": "e144be20-01d8-4fdc-9eb7-5ca255035c4b",
      "sellerId": "O4fgEI93QqYjs3IBdvUeS12JqbA3",
      "payerId": "Yf7Ahs5DOJRTLvFf84s4uOp7B7Q2",
      "type": "free",
      "status": "inactive",
      "billingCycleMonths": 1,
      "credits": 0,
      "autoRenew": true,
      "freeTrial": false,
      "activatedAt": "2024-03-28T15:46:46.839Z",
      "modifiedAt": "2024-03-28T15:46:47.436Z",
      "createdAt": "2024-03-28T15:46:47.436Z",
      "version": 4
    },
    "user": {
      "id": "Yf7Ahs5DOJRTLvFf84s4uOp7B7Q2",
      "firstName": "John",
      "lastName": "Doe",
      "document": "08351973955",
      "email": "john.doe@hub.la",
      "phone": "+5511988646782"
    }
  },
  "version": "2.0.0"
}
```

{% endtab %}

{% tab title="FreeTrial" %}

```json
{
  "type": "customer.member_removed",
  "event": {
    "product": {
      "id": "inAVzweR0QYw5y03K5mq",
      "name": "Integrações com Webhook 2.0"
    },
    "products": [{
      "id": "inAVzweR0QYw5y03K5mq",
      "name": "Integrações com Webhook 2.0",
      "offers": [{
        "id": "inAVzweR0QYw5y03K5mq",
        "name": "Principal",
        "cohorts": [{ "id": "3a96c85e-cf82-4236-b242-7431f405c521" }]
      }]
    }],
    "subscription": {
      "id": "e144be20-01d8-4fdc-9eb7-5ca255035c4b",
      "sellerId": "O4fgEI93QqYjs3IBdvUeS12JqbA3",
      "payerId": "Yf7Ahs5DOJRTLvFf84s4uOp7B7Q2",
      "type": "recurring",
      "status": "inactive",
      "billingCycleMonths": 1,
      "credits": 0,
      "paymentMethod": "credit_card",
      "autoRenew": true,
      "freeTrial": true,
      "activatedAt": "2024-03-28T15:46:46.839Z",
      "modifiedAt": "2024-03-28T15:46:47.436Z",
      "createdAt": "2024-03-28T15:46:47.436Z",
      "firstPaymentSession": {
        "ip": "220.172.165.140",
        "utm": {
          "source": "email",
          "medium": "active-campaign",
          "campaign": "[LEAD][QUENTE][24][MAR]",
          "content": "2024032812H",
          "term": "TRIAL7"
        }
      },
      "version": 4
    },
    "user": {
      "id": "Yf7Ahs5DOJRTLvFf84s4uOp7B7Q2",
      "firstName": "John",
      "lastName": "Doe",
      "document": "08351973955",
      "email": "john.doe@hub.la",
      "phone": "+5511988646782"
    }
  },
  "version": "2.0.0"
}
```

{% endtab %}
{% endtabs %}

## Propriedades

Os eventos de membro seguem um padrão de payload e propriedades, sendo elas:

{% tabs %}
{% tab title="Propriedades" %}
**type** `string`

Tipo do evento de Webhook

<table><thead><tr><th width="279">Valores possíveis</th><th>Descrição</th></tr></thead><tbody><tr><td>customer.member_added</td><td>Acesso concedido</td></tr><tr><td>customer.member_removed</td><td>Acesso removido</td></tr></tbody></table>

***

**version** `string`

Versão do contrato do payload. Neste caso o valor esperado será sempre `v2.0.0`.

***

**event.product** `object`

Representa as informações do produto comprado

***

**event.product.id** `string`

Identificador único do produto

***

**event.product.name** `string`

Nome do produto no momento da compra

***

**event.subscription.id** `string`

Identificador único da assinatura

***

**event.subscription.sellerId** `string`

Identificador único do vendedor

***

**event.subscription.payerId** `string`

Identificador único do comprador

***

**event.subscription.type** `string`

Tipo da assinatura

<table><thead><tr><th width="199">Valores possíveis</th><th>Descrição</th></tr></thead><tbody><tr><td>recurring</td><td>Renovação</td></tr><tr><td>one_time</td><td>Pagamento único</td></tr><tr><td>free</td><td>Assinatura gratuita</td></tr></tbody></table>

***

**event.subscription.status** `string`

Status da assinatura

<table><thead><tr><th width="193">Valores possíveis</th><th>Descrição</th></tr></thead><tbody><tr><td>active</td><td>Assinatura está ativa e possuí créditos</td></tr><tr><td>inactive</td><td>Assinatura está inativa e não possuí créditos</td></tr></tbody></table>

***

**event.subscription.billingCycleMonths** `integer`

Quantidade de meses que a assinatura renova

<table><thead><tr><th width="201">Valores possíveis</th><th>Descrição</th></tr></thead><tbody><tr><td>1</td><td>Mensal</td></tr><tr><td>3</td><td>Trimestral</td></tr><tr><td>6</td><td>Semestral</td></tr><tr><td>12</td><td>Anual</td></tr></tbody></table>

***

**event.subscription.credits** `integer`

Quantidade de créditos disponíveis na assinatura. Cada unidade de crédito representa um dia.

***

**event.subscription.paymentMethod** `string`

Metodo de pagamento utilizado

<table><thead><tr><th width="201">Valores possíveis</th><th>Descrição</th></tr></thead><tbody><tr><td>credit_card</td><td>Cartão de crédito</td></tr><tr><td>pix</td><td>Pix</td></tr><tr><td>bank_slip</td><td>Boleto</td></tr></tbody></table>

***

**event.subscription.autoRenew** `boolean`

Representa se a assinatura está com a renovação automática ativada, caso esteja desativa quando se esgotarem os créditos não irá efetuar a renovação automática

***

**event.subscription.freeTrial** `boolean`

Representa se a assinatura está em um período de teste

***

**event.subscription.activatedAt** `string`

Representa a última data que a assinatura ficou com o status ativa, segue o padrão de ISO-8601 com UTC 0

***

**event.subscription.inactivatedAt** `string`

Representa a última data que a assinatura ficou com o status inativa, segue o padrão de ISO-8601 com UTC 0

***

**event.subscription.deactivatedAutoRenewAt** `string`

Representa a última data do cancelamento da renovação automática, segue o padrão de ISO-8601 com UTC 0

***

**event.subscription.reactivatedAutoRenewAt** `string`

Representa a última data de reativação da renovação automática, segue o padrão de ISO-8601 com UTC 0

***

**event.subscription.modifiedAt** `string`

Representa a data da última atualização da assinatura, segue o padrão de ISO-8601 com UTC 0

***

**event.subscription.createdAt** `string`

Quando a assinatura foi criada, segue o padrão de ISO-8601 com UTC 0

***

**event.subscription.version** `integer`

Contador que reflete a versão atual da assinatura. Para uma assinatura que foi atualizada 50 vezes, espera que o seu valor seja 50.

***

**event.subscription.firstPaymentSession** `object`

Representa as informações capturadas do comprador no momento da compra.

***

**event.subscription.firstPaymentSession.ip** `string`

IP do comprador no momento de compra

***

**event.subscription.firstPaymentSession.utm.source** `string`

Representa o valor de `utm_source` capturado no momento da compra

***

**event.subscription.firstPaymentSession.utm.medium** `string`

Representa o valor de `utm_medium` capturado no momento da compra

***

**event.subscription.firstPaymentSession.utm.campaign** `string`

Representa o valor de `utm_campaign` capturado no momento da compra

***

**event.subscription.firstPaymentSession.utm.content** `string`

Representa o valor de `utm_content` capturado no momento da compra

***

**event.subscription.firstPaymentSession.utm.term** `string`

Representa o valor de `utm_term` capturado no momento da compra

***

**event.user** `object`

Representa as informações de usuário cadastradas na plataforma

***

**event.user.id** `string`

Identificador único do comprador

***

**event.user.firstName** `string`

Primeiro nome do comprador

***

**event.user.lastName** `string`

Sobrenome nome do comprador

***

**event.user.document** `string`

Representa o documento de identificação do comprador, podendo ser do tipo CPF, CNPJ ou nulo

***

**event.user.email** `string`

Email do comprador

***

**event.user.phone** `string`

Telefone com DDI e DDD do comprador
{% endtab %}
{% endtabs %}

***
