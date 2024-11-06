from django.shortcuts import render
from .models import Monster

# Create a monster entry
def create_monster(name, monster_type, description, habitat, danger_level):
    return Monster.objects.create(
        name=name,
        monster_type=monster_type,
        description=description,
        habitat=habitat,
        danger_level=danger_level
    )

# Read all monsters
def read_all_monsters():
    return Monster.objects.all()

# Search monsters by keyword
def search_monsters(keyword):
    return Monster.objects.filter(
        name = keyword
    )

# Read a single monster by ID
def read_monster_by_id(monster_id):
    try:
        return Monster.objects.get(id=monster_id)
    except Monster.DoesNotExist:
        return None

# Update a monster entry by ID
def update_monster(monster_id, new_name=None, new_monster_type=None, new_description=None, new_habitat=None, new_danger_level=None):
    monster = read_monster_by_id(monster_id)
    if monster:
        if new_name:
            monster.name = new_name
        if new_monster_type:
            monster.monster_type = new_monster_type
        if new_description:
            monster.description = new_description
        if new_habitat:
            monster.habitat = new_habitat
        if new_danger_level:
            monster.danger_level = new_danger_level
        monster.save()
        return monster
    return None

# Delete a monster entry by ID
def delete_monster(monster_id):
    monster = read_monster_by_id(monster_id)
    if monster:
        monster.delete()
        return True
    return False
