import wunderpy2
api = wunderpy2.WunderApi()
client = api.get_client("1415217427f971fdcec70ac983d37ef5318dc9f47a8a26ef9b20760aa90f", "2861fdd42c28ce54ef91")

lists = client.get_lists()
print(lists)

# lists = client.get_lists()
# list = lists[0]
task = client.create_task(1234, "My new task", due_date="2019-08-02", starred=True)
# client.create_note(task[wunderpy2.Task.ID], "My note")
# client.create_subtask(task[wunderpy2.Task.ID], "My subtask")ss