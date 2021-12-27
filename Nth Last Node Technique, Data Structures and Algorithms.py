# from LinkedList import LinkedList

# Complete this function:
def nth_last_node(linked_list, n):
  nth_last_node = None
  count = 1
  tail_pointer = linked_list.head_node

  while tail_pointer:
    count += 1
    tail_pointer = tail_pointer.get_next_node()
    if count >= n + 1:
      if nth_last_node == None:
        nth_last_node = linked_list.head_node
      else:
        nth_last_node = nth_last_node.get_next_node()
  return nth_last_node



def generate_test_linked_list():
  linked_list = LinkedList()
  for i in range(50, 0, -1):
    linked_list.insert_beginning(i)
  return linked_list

# Use this to test your code:
test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 4)
print(nth_last.value)