[![Build](https://img.shields.io/badge/dev-gorpo-brightgreen.svg)]()
[![Stage](https://img.shields.io/badge/Release-Stable-brightgreen.svg)]()
[![Build](https://img.shields.io/badge/python-v3.7-blue.svg)]()
[![Build](https://img.shields.io/badge/windows-7%208%2010-blue.svg)]()
[![Build](https://img.shields.io/badge/Linux-Ubuntu%20Debian-orange.svg)]()
[![Build](https://img.shields.io/badge/arquiterura-64bits-blue.svg)]()
<h2 align="center">Manicomio Telegram Heroku Bot</h2>
## Instruções:
1. Edite no arquivo config se quer rodar o bot local ou no heroku, comente e descomente as linhas.
2. Edite requeriments.txt caso tenha adicionado novas libs.
3. Especifique a versão do python no arquivo runtime, confira as versões de python disponiveis no heroku [aqui](https://devcenter.heroku.com/articles/python-runtimes)
4. Crie um bot no Botfather e pegue o token do bot.
5. insira este bot em um canal e pegue o id do canal, ele servirá para os logs.
6. pegue sua id ela servirá para você ser adm master.

### Via linha de comando - CLI
```
cd manicomio_bot_heroku
heroku login
heroku create --region us manicomio       #seta us como regiao e nome_do_app defina o nome do  app no heroku
heroku buildpacks:set heroku/python       #seta o python
git push heroku master                    #deploy do programa no heroku

heroku config:set TELEGRAM_TOKEN=1186597860:AAHZTQT--xYhNHhkO8SbxlSxrdwVnkvi38s #seta as config vars, insira seu token
heroku config:set LOGS=-1001215401730    #seta a id do canal de logs que o bot ja deve estar e ter admin
heroku config:set SUDOERS=522510051      #seta o sudo ou seja adm master do bot

heroku ps:scale bot=1 # start bot dyno - inicia seu bot
heroku logs --tail # Ativa os logs no terminal ou cmd
heroku ps:stop bot #para o bot dyno  - para seu bot
```

### links uteis
- https://devcenter.heroku.com/articles/dynos
- https://devcenter.heroku.com/articles/config-vars
- https://devcenter.heroku.com/articles/heroku-redis
- https://devcenter.heroku.com/articles/error-codes



## Deploying via [Heroku Dashboard](https://dashboard.heroku.com) (GUI)
1. [Fork](https://github.com/gorpo/manicomio_bot_heroku/fork) este repositorio.
3. Vá para [Painel] (https://dashboard.heroku.com), faça login, Pressione _Novo_ e escolha _Criar novo aplicativo._
4. Preencha um _App Name_ e escolha _Runtime Region._
5. Conecte seu repositório GitHub na página _Deploy_.
6. Configuração ** Automatics deploys ** _ (Opcionalmente) ._
7. _Implante uma filial do GitHub._
8. Em seguida, vá para uma página _Settings_, clique em _Reveal Config Vars_ e adicione seus próprios, por exemplo:
! [Config Vars] (http://i.imgur.com/C3cmphh.png)
9. ** Finalmente **, vá para a página _Resources_.
    1. Instale o _Heroku Redis_ add-on _ (Opcionalmente) _
    2. Pressione um botão pequeno da caneta, mova o controle deslizante e clique em _Confirmar_, que iniciará o bot dyno.
    3. Simplesmente mova o controle deslizante para trás se precisar parar o bot dyno, lembre-se de clicar em _Confirmar_.
    4. Se, por algum motivo, não estiver funcionando, verifique os logs aqui
    ! [Logs] (http://i.imgur.com/rIHU6zF.png)
