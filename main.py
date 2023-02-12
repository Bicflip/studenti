import Service.studentservice
import UI.console
import Repository.studentrepo

repo = Repository.studentrepo.StudentRepo()
services = Service.studentservice.StudentServices(repo)
Ui = UI.console.user_interface(services)

Ui.consola()
