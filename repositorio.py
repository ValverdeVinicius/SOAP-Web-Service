class DisciplinasRepo:
    def __init__(self):
        self.repo = {
            "Webservices":
                ["Conceitos de Web Services",
                "Utilizando SOAP em Java",
                "Utilizando REST em Java"],
            "Programação Servidor com Java":
                ["Webserver Tomcat",
                 "App Server GlassFish",
                 "Servlet e JSP"],
            "JPA e JEE":
                ["Tecnologia JPA",
                 "Enterprise Java Beans",
                 "Arquitetura MVC"]
        }
    def getTemas(self):
        return self.repo.keys()
    def getModulosTema(self, tema):
        return self.repo[tema]
