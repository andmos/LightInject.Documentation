
import subprocess

def download(url, file):
    outfile = open(file, "wb")
    subprocess.call(["curl", url], stdout=outfile)

download('https://raw.githubusercontent.com/seesharper/LightInject/master/readme.md', 'docs/index.md')
download('https://raw.githubusercontent.com/seesharper/LightInject/master/designpatterns.md', 'docs/designpatterns.md')
download('https://raw.githubusercontent.com/seesharper/LightInject.Documentation/master/licence.md', 'docs/licence.md')
download('https://raw.githubusercontent.com/seesharper/LightInject.xUnit/master/readme.md', 'docs/xunit.md')
download('https://raw.githubusercontent.com/seesharper/LightInject.AutoFactory/master/readme.md', 'docs/autofactory.md')
download('https://raw.githubusercontent.com/seesharper/LightInject.Annotation/master/readme.md', 'docs/annotation.md')
download('https://raw.githubusercontent.com/seesharper/LightInject.Interception/master/readme.md', 'docs/interception.md')
download('https://raw.githubusercontent.com/seesharper/LightInject.WebApi/master/readme.md', 'docs/webapi.md')
download('https://raw.githubusercontent.com/seesharper/LightInject.SignalR/master/readme.md', 'docs/signalr.md')
download('https://raw.githubusercontent.com/seesharper/LightInject.Nancy/master/readme.md', 'docs/nancy.md')
download('https://raw.githubusercontent.com/seesharper/LightInject.Web/master/readme.md', 'docs/web.md')
download('https://raw.githubusercontent.com/seesharper/LightInject.Wcf/master/readme.md', 'docs/wcf.md')
download('https://raw.githubusercontent.com/seesharper/LightInject.Mvc/master/readme.md', 'docs/mvc.md')
download('https://raw.githubusercontent.com/seesharper/LightMock/master/readme.md', 'docs/lightmock.md')
download('https://raw.githubusercontent.com/seesharper/LightInject.Microsoft.DependencyInjection/master/readme.md', 'docs/microsoft.dependencyinjection.md')
download('https://raw.githubusercontent.com/seesharper/LightInject.Microsoft.AspNetCore.Hosting/master/README.md', 'docs/microsoft.aspnetcore.hosting.md')
download('https://raw.githubusercontent.com/seesharper/Blog.WebApiRequestLogging/master/readme.md', 'docs/webapirequestlogging.md')
download('https://raw.githubusercontent.com/seesharper/Blog.Transactions/master/readme.md', 'docs/transactions.md')
download('https://raw.githubusercontent.com/seesharper/Blog.AspNetCoreUnitTesting/master/readme.md', 'docs/aspnetcoreunittesting.md')
download('https://raw.githubusercontent.com/seesharper/Blog.DotNet-Steps/master/README.md', 'docs/blog-dotnet-steps.md')
