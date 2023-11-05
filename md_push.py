api = HubApi()
api.login(YOUR_ACCESS_TOKEN)
api.push_model(
    model_id="CiMing/Ava", 
    model_dir="trained_model" # 本地模型目录，要求目录中必须包含configuration.json
)
