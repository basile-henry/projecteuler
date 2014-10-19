def mergesort(list_a, list_b):
	out = []
	i = 0
	j = 0

	while True:

		if list_a[i] < list_b[j]:
			out.append(list_a[i])
			i+=1
		else:
			out.append(list_b[j])
			j+=1

		if i == len(list_a):
			out += list_b[j:]
			break
		if j == len(list_b):
			out += list_a[i:]
			break

	return out


def sort(my_list):
	n = len(my_list)

	if n <= 1:
		return my_list

	return mergesort(sort(my_list[:n/2]), sort(my_list[n/2:]))

print sort([3,5,4,1,2,7,8,998,5,4,2,11,45,4,77])