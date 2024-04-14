from tasks import add_two_num

result = add_two_num.delay(3, 5)

print(result.__getstate__()['on_ready'])
