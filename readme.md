#Godroid#
###Instalação###
```
pip install -r requirements.txt
```

###Registrar o app###
**project/setting.py**
```
INSTALLED_APPS = [
    'django.contrib.admin',
	...
    'app',
]
```
###Registrar as urls###
**project/urls.py**
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]
```
###Criar a pasta 'templates'###

###Configurar modelos / 'views'###
-Criar a pasta 'models'
-Importar os arquivos no __init__.py
-Deletar 'models.py'

###Configurar formulários
```
pip install django-widget-tweaks
```
```
INSTALLED_APPS = [
    'widget_tweaks',
]
```