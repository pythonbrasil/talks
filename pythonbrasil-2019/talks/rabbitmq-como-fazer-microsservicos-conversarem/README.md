# Python Brasil 2019 . Palestras


A palestra **RabbitMQ, como fazer microsserviços conversarem** foi apresentada no dia 26/10/2019, durante a [Conferência Python Brasil 2019](http://2019.pythonbrasil.org.br).


## RabbitMQ, como fazer microsserviços conversarem
Apresentada por: **João Daher Neto**

### Slides
Acesse os slides: **[RabbitMQ, como fazer microsserviços conversarem](./pybr2019-joao-daher-neto-rabbitmq-como-fazer-microsservicos-conversarem.pdf)**


### Sobre Palestra
Microsserviços, por definição, devem ser pequenos, sem estado e independentes. Muitos erros comuns acontecem ao tentar comunicar serviços distintos. Ao implementar troca de dados sempre de forma síncrona, esquece-se de que um serviço não deve assumir do estado de outro, causando um efeito em cadeia de dependência. Outros optam pela simplicidade de isolar a aplicação, mas agregar os dados em uma única fonte.


A maior dificuldade na migração de um monolito para um ecossistema de microsserviços está em garantir a independência, fazendo com que cada aplicação tenha um domínio de dados bem definido. Mas como isolar aplicações que precisam constantemente trocar informações?

Irei abordar um caso de uso de como o time da eduK arquitetou a comunicação entre microsserviços Python utilizando um serviço de mensageria de protocolo AMQP (RabbitMQ, CloudAMQP, Kafka) através do padrão PubSub. Esta palestra tem o intuito de apontar problemas comuns de configuração e demonstrar boas práticas de implementações a serem consideradas para manter a saúde e integridade dos dados no universo de aplicações.




