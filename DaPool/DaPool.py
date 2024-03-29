import time

class Projectile:
    def __init__(self):
        self.is_active = False

    def activate(self):
        self.is_active = True
        print("Projectile activated")

    def deactivate(self):
        self.is_active = False
        print("Projectile deactivated")


class ProjectilePool:
    def __init__(self, pool_size):
        self.pool = [Projectile() for _ in range(pool_size)]

    def get_projectile(self):
        for projectile in self.pool:
            if not projectile.is_active:
                projectile.activate()
                return projectile
        time.sleep(1)  
        return self.get_projectile()

    def recycle_projectile(self, projectile):
        projectile.deactivate()

if __name__ == "__main__":
    projectile_pool = ProjectilePool(pool_size=5)

    player_projectile1 = projectile_pool.get_projectile()
    player_projectile2 = projectile_pool.get_projectile()
    player_projectile3 = projectile_pool.get_projectile()

    time.sleep(2)

    projectile_pool.recycle_projectile(player_projectile1)
    projectile_pool.recycle_projectile(player_projectile2)
    projectile_pool.recycle_projectile(player_projectile3)

    player_projectile4 = projectile_pool.get_projectile()
    player_projectile5 = projectile_pool.get_projectile()

    time.sleep(1)
    
    projectile_pool.recycle_projectile(player_projectile4)
    projectile_pool.recycle_projectile(player_projectile5)
