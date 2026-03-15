from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription

class Gym:
    def __init__(self):
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipments: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []

    def __add_item(self, item, collection) -> None:
        if item not in collection:
            collection.append(item)

    def add_customer(self, customer: Customer):
        self.__add_item(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.__add_item(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        self.__add_item(equipment, self.equipments)

    def add_plan(self, plan: ExercisePlan):
        self.__add_item(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        self.__add_item(subscription, self.subscriptions)

    def subscription_info(self, subscription_id: int):
        subscription = next((s for s in self.subscriptions if subscription_id == s.id),None)
        customer = next((c for c in self.customers if c.id == subscription.customer_id), None)
        trainer = next((t for t in self.trainers if t.id == subscription.trainer_id), None)
        plan = next((p for p in self.plans if p.id == subscription.exercise_id), None)
        equipment = next((e for e in self.plans if e.id == plan.equipment_id), None)
        return "\n".join(subscription.__repr__() + customer.__repr__() + trainer.__repr__() + equipment.__repr__() + plan.__repr__())



