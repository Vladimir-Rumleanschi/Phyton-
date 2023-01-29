class BTreeNode(object): 
	def __init__(self, values): 
		self.values = values
		self.children = []
	
	def add_child(self, child_values):
		self.children.append(BTreeNode(child_values))
		self.children.sort()

	def add_value(self, value):
		self.values.append(value)
		self.values.sort()

	def remove_value(self, value):
		self.values.remove(value)
	
	def __lt__(self, other):
		return self.values[-1] < other.values[-1]

	def draw(self, root_node=True):
		my_str=''
		if root_node:
			my_str = '''
			          	<!DOCTYPE html>
					<html lang="en">
					  <head>
					    <meta charset="utf-8">

					    <title>Collapsible Tree Example</title>

					    <style>

						.node circle {
						  fill: #fff;
						  stroke: steelblue;
						  stroke-width: 3px;
						}

						.node text { font: 12px sans-serif; }

						.link {
						  fill: none;
						  stroke: #ccc;
						  stroke-width: 2px;
						}
						
					    </style>

					  </head>

					  <body>

					<!-- load the d3.js library -->	
					<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.17/d3.min.js"></script>
						
					<script>

					var treeData = [
					  '''
	
		my_str += '{"name": "'
		for v in self.values:
			my_str += str(v) + ', '
		my_str = my_str[:-2]
		my_str += '" '

		if len(self.children) > 0:
			my_str += ', "children": ['

		value_id = 0		
		for child in self.children:
			my_str += child.draw(root_node=False) + ', '
		
		if len(self.children) > 0:
			my_str += ']'
		
		my_str += '}'

		
		if root_node:
			my_str += '''
			];

			// ************** Generate the tree diagram	 *****************
			var margin = {top: 40, right: 120, bottom: 20, left: 120},
				width = 1500 - margin.right - margin.left,
				height = 800 - margin.top - margin.bottom;
				
			var i = 0;

			var tree = d3.layout.tree()
				.size([height, width]);

			var diagonal = d3.svg.diagonal()
				.projection(function(d) { return [d.x, d.y]; });

			var svg = d3.select("body").append("svg")
				.attr("width", width + margin.right + margin.left)
				.attr("height", height + margin.top + margin.bottom)
			  .append("g")
				.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

			root = treeData[0];
			  
			update(root);

			function update(source) {

			  // Compute the new tree layout.
			  var nodes = tree.nodes(root).reverse(),
				  links = tree.links(nodes);

			  // Normalize for fixed-depth.
			  nodes.forEach(function(d) { d.y = d.depth * 100; });

			  // Declare the nodes…
			  var node = svg.selectAll("g.node")
				  .data(nodes, function(d) { return d.id || (d.id = ++i); });

			  // Enter the nodes.
			  var nodeEnter = node.enter().append("g")
				  .attr("class", "node")
				  .attr("transform", function(d) { 
					  return "translate(" + d.x + "," + d.y + ")"; });

			  nodeEnter.append("circle")
				  .attr("r", 10)
				  .style("fill", "#fff");

			  nodeEnter.append("text")
				  .attr("y", function(d) { 
					  return d.children || d._children ? -18 : 18; })
				  .attr("dy", ".35em")
				  .attr("text-anchor", "middle")
				  .text(function(d) { return d.name; })
				  .style("fill-opacity", 1);

			  // Declare the links…
			  var link = svg.selectAll("path.link")
				  .data(links, function(d) { return d.target.id; });

			  // Enter the links.
			  link.enter().insert("path", "g")
				  .attr("class", "link")
				  .attr("d", diagonal);

			}

			</script>
				
			  </body>
			</html>

			'''
		
			with open('tree.html', 'w+') as fp:
    				fp.write(my_str)
			from IPython.display import IFrame

			return IFrame(src='./tree.html', width=1500, height=400)
		else:
			return my_str
    
    
