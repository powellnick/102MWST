#!/usr/local/bin/python3

import sys

def read_input(file_name):
	with open(file_name, 'r') as file:
		n = int(file.readline().strip())
		m = int(file.readline().strip())
		edges = []
		for i in range(m):
			x, y, w = file.readline().strip().split()
			edges.append((int(x), int(y), float(w), i + 1))
	return n, m, edges

def find(parent, i):
	if parent[i] == i:
		return i
	else:
		return find(parent, parent[i])

def union(parent, rank, x, y):
	root_x = find(parent, x)
	root_y = find(parent, y)
	
	if rank[root_x] < rank[root_y]:
		parent[root_x] = root_y
	elif rank[root_x] > rank[root_y]:
		parent[root_y] = root_x
	else:
		parent[root_y] = root_x
		rank[root_x] += 1

def kruskal(n, edges):
	edges.sort(key=lambda edge: edge[2])
	parent = list(range(n + 1))
	rank = [0] * (n + 1)
	
	mst = []
	mst_weight = 0
	
	for edge in edges:
		u, v, weight, label = edge
		root_u = find(parent, u)
		root_v = find(parent, v)
		
		if root_u != root_v:
			union(parent, rank, root_u, root_v)
			mst.append(edge)
			mst_weight += weight
			
	return mst, mst_weight

def write_output(file_name, mst, total_weight):
	with open(file_name, 'w') as file:
		for edge in mst:
			u, v, weight, label = edge
			file.write(f"{label:4}: ({u}, {v}) {weight:.1f}\n")
		file.write(f"Total Weight = {total_weight:.2f}\n")

def main():
	if len(sys.argv) != 3:
		print("Usage: MWST input_file output_file")
		return
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	
	n, m, edges = read_input(input_file)
	mst, total_weight = kruskal(n, edges)
	write_output(output_file, mst, total_weight)

if __name__ == "__main__":
	main()
