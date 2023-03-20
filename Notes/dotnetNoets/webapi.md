# webapi





```C#
Scaffold-DbContext "Server=SMGSQL01;Database=SkyView;Trusted_Connection=True;User ID=ckyview;Password=Idced@11ic;Trusted_Connection=True;TrustServerCertificate=True" Microsoft.EntityFrameworkCore.SqlServer -OutputDir Models -Force
```

## app.setting

```C#
  "ConnectionStrings": {
    "SkyViewDataBase": "Server=SMGSQL01;Database=SkyView;User ID=ckyview;Password=Idced@11ic;Trusted_Connection=True;TrustServerCertificate=True"
  }
```

## program.cs

```C#
using apiTest.Models;
using Microsoft.EntityFrameworkCore;
builder.Services.AddDbContext<SkyViewContext>(opt =>opt.UseSqlServer(builder.Configuration.GetConnectionString("SkyViewDataBase")));
```



## 例子代碼

```C#
using apiTest.Models;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace apiTest.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class HelloWorldController : ControllerBase
    {


        private readonly SkyViewContext _skyViewContext;

        public HelloWorldController(SkyViewContext skyViewContext)
        {
            _skyViewContext = skyViewContext;

        }
        
        //[HttpGet]
        //public IEnumerable<Tgirvc> Get()
        //{
        //    return _skyViewContext.Tgirvcs.ToList();
        //}
        [HttpGet]
        public ActionResult<IEnumerable<Tgirvc>> Get()
        {
            return _skyViewContext.Tgirvcs;
        }



        [HttpGet("{ObsDatetime}")]
        public IEnumerable<Tgirvc> Get(string ObsDatetime)
        {
            //var result = _skyViewContext.Tgirvcs.Find(ObsDatetime);
            //if (result == null)
            //{
            //    return NotFound("找不到資料");
            //}

            var result=from a in _skyViewContext.Tgirvcs
                       where a.ObsDatetime== "2022-06-02 00:00:00"
                       select a;


            var result2 = _skyViewContext.Tgirvcs.Where(a => a.ObsDatetime == "2022-06-01 00:00:00");

            return result;
        }
    }
}
```