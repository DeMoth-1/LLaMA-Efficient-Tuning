from modelscope.hub.api import HubApi

YOUR_ACCESS_TOKEN = '088e197c-a9fb-4f89-9fde-b921934294f2'
api = HubApi()
api.login(YOUR_ACCESS_TOKEN)
from modelscope.hub.snapshot_download import snapshot_download

model_dir = snapshot_download(model_ID = 'CiMing/glm3', cache_dir='glm3', revision='master')
