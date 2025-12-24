class InstanceService:
    def __init__(self, client):
        self.client = client

    def fetch_instances(self):
        return self.client.get('instance/fetchInstances')

    def create_instance(self, config):
        return self.client.post('instance/create', data=config.__dict__)

    def set_webhook(self, instance_name: str, config, instance_token):
        data = {'webhook': config.__dict__}
        return self.client.post(f"webhook/set/{instance_name}", data=data)

    def set_events(self, instance_name: str, config, instance_token: str):
        return self.client.post(
            f'instance/{instance_name}/{instance_token}/setEvents', data=config.__dict__
        )
