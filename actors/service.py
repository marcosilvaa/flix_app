from actors.repository import ActorRepository

class ActorService:
    
    def __init__(self):
        self.actor_repository = ActorRepository()
        
    
    def get_actors(self):
        return self.actor_repository.get_actors()
    
    
    def create_actor(self, actor):
        actor = dict(
            name=actor,
        )
        return self.actor_repository.create_actor(actor)
    