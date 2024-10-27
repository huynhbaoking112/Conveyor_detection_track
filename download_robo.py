

from roboflow import Roboflow
rf = Roboflow(api_key="sReAjhDKWPObR6HdlQEQ")
project = rf.workspace("kinghuynh").project("conveyor-lg5wk")
version = project.version(1)
dataset = version.download("yolov8")
                