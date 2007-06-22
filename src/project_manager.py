class ProjectManager:
	def __init__(self):
		self.projects = []

	def createProject(self, name, path):
		#check if project DB already exists
		os.path.exists(path+os.pathsep+name)
		
		#Create project
		proj = Project(name)
		projects.append(project)
		
		#Copy template db as new db