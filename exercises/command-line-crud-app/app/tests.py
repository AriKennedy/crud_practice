from django.test import TestCase
from .models import Monster
from .views import create_monster, read_all_monsters, search_monsters, read_monster_by_id, update_monster, delete_monster

class MonsterModelTest(TestCase):

    def setUp(self):
        # Set up initial data for tests
        create_monster("Succubus", "Demon", "A seductive demon that feeds on life force.", "Dungeons", 5)
        create_monster("Kitsune", "Beast", "A fox spirit known for its tricks and illusions.", "Forests", 3)

    def test_create_monster(self):
        monster = create_monster("Mermaid", "Aquatic", "A sea creature with the upper body of a human and the lower body of a fish.", "Oceans", 2)
        self.assertEqual(monster.name, "Mermaid")
        self.assertEqual(monster.monster_type, "Aquatic")
        self.assertEqual(Monster.objects.count(), 3)  # Two from setUp + one new

    def test_read_all_monsters(self):
        monsters = read_all_monsters()
        self.assertEqual(len(monsters), 2)

    def test_search_monsters(self):
        
        result = search_monsters("Succubus")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Succubus")

    def test_read_monster_by_id(self):
        monster = Monster.objects.first()
        fetched_monster = read_monster_by_id(monster.id)
        self.assertIsNotNone(fetched_monster)
        self.assertEqual(fetched_monster.name, monster.name)

        self.assertIsNone(read_monster_by_id(999))  # Non-existent ID

    def test_update_monster(self):
        monster = Monster.objects.first()
        updated_monster = update_monster(monster.id, new_name="Greater Succubus", new_danger_level=5)
        self.assertEqual(updated_monster.name, "Greater Succubus")
        self.assertEqual(updated_monster.danger_level, 5)

    def test_delete_monster(self):
        monster = Monster.objects.first()
        delete_monster(monster.id)
        self.assertEqual(Monster.objects.count(), 1)  # One monster should be deleted
