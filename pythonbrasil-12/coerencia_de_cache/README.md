Coerência de cache de granuraridade fina, usando django-signals
===============================================================

Autor: Helber Maciel Guerra
twitter: @helbermg
github: helber
E-Mail: helbermg@gmail.com

Fazendo o uso do cache do nginx, podemos ter melhoria de desempenho de APIs restful e conteúdos de 1000X ou mais. Mas como ter controle do que está no cache e se este conteúdo é coerente com o que está no backend?
Com sistemas de cache utilizando nginx ou varnish, geralmente são baseados em tempo (valid 10 min., 24h, ...) mas muitas vezes ao fazer modificações em models do django, seria muito bom que este cache fosse invalidado no momento da modificação (post_save, post_delete, pre_save, etc).
O django-cache-coherence foi criado para atender esta necessidade. Para cada requisição em uma url requisitada e está configurada para fazer cache, os dados da requisição são salvos em um banco e registrado um signal para fazer a limpeza deste cache (PURGE). Assim que houver uma chamada do signal registrado, é feito uma consulta neste banco de requisições cacheadas, e disparado as limpezas, invalidando o cache somente da informação modificada, deixando integro o restante ndo cache.
Para ativar este tipo de funcionalidade no nginx é utilizado o módulo [ngx_cache_purge](https://github.com/FRiCKLE/ngx_cache_purge/)
Vou mostrar a configuração do nginx e como fazer inclusive cache de APIs, com e sem autenticação. Mostrando como garantir e entrega com cache de informações sensiveis de usuários.
Para a validação de verificação do funcionamento são feitos testes de integração com testes unitários e containers docker.

Para ver os slides acesse: https://speakerdeck.com/helber/coerencia-de-cache-de-granularidade-fina-usando-django-signals

