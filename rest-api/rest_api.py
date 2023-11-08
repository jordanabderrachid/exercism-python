import json


class RestAPI:
    def __init__(self, database=None):
        self.database = database or {"users": []}

    def get(self, url, payload=None):
        if url == "/users":
            if payload is None:
                return json.dumps(self.database)

            payload = json.loads(payload)
            users = []
            for name in payload["users"]:
                users.append(self._get_user_info(name))

            return json.dumps({"users": users})

        pass

    def post(self, url, payload=None):
        if url == "/add":
            payload = json.loads(payload or "{}")
            return json.dumps(self._add_user(payload["user"]))

        if url == "/iou":
            payload = json.loads(payload or "{}")
            self._record_iou(payload["lender"], payload["borrower"], payload["amount"])
            users = [
                self._get_user_info(n)
                for n in sorted([payload["lender"], payload["borrower"]])
            ]
            return json.dumps({"users": users})

        pass

    def _add_user(self, name):
        self.database["users"].append(
            {"name": name, "owes": {}, "owed_by": {}, "balance": 0.0}
        )
        return self._get_user_info(name)

    def _get_user_info(self, name):
        for user in self.database["users"]:
            if user["name"] == name:
                return user

        return None

    def _record_iou(self, lender_name, borrower_name, amount):
        lender = self._get_user_info(lender_name)
        lender["balance"] += amount
        if borrower_name in lender["owes"]:
            owed_amount = lender["owes"][borrower_name]
            owed_amount -= amount
            if owed_amount > 0:
                lender["owes"][borrower_name] = owed_amount
            elif owed_amount < 0:
                lender["owes"].pop(borrower_name)
                lender["owed_by"][borrower_name] = -owed_amount
            else:
                lender["owes"].pop(borrower_name)
        else:
            if borrower_name in lender["owed_by"]:
                lender["owed_by"][borrower_name] += amount
            else:
                lender["owed_by"][borrower_name] = amount

        borrower = self._get_user_info(borrower_name)
        borrower["balance"] -= amount
        if lender_name in borrower["owed_by"]:
            owed_amount = borrower["owed_by"][lender_name]
            owed_amount -= amount
            if owed_amount > 0:
                borrower["owed_by"][lender_name] = owed_amount
            elif owed_amount < 0:
                borrower["owed_by"].pop(lender_name)
                borrower["owes"][lender_name] = -owed_amount
            else:
                borrower["owed_by"].pop(lender_name)
        else:
            if lender_name in borrower["owes"]:
                borrower["owes"][lender_name] += amount
            else:
                borrower["owes"][lender_name] = amount

        self._update_user(lender)
        self._update_user(borrower)

    def _update_user(self, user):
        for i, u in enumerate(self.database["users"]):
            if u["name"] == user["name"]:
                self.database["users"][i] = user
                break
