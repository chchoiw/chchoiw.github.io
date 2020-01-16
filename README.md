[Welcome to my homepage!](https://chchoiw.github.io/)
- mathjax fix '$','$' not show math

```javascript
<script type="text/x-mathjax-config"> MathJax.Hub.Config({ TeX: { equationNumbers: { autoNumber: "all" } } }); </script>
<script type="text/x-mathjax-config">

  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['$','$'], ["\\(","\\)"] ],
      displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
      processEscapes: true
    }
  });

``` 
- mathjax fix ```CDATA```
add _inclue/footer/金山尸廿.html
```javascript
     <script type="text/x-mathjax-config">
     MathJax.Hub.Register.StartupHook("TeX Jax Ready",function () {
       MathJax.InputJax.TeX.prefilterHooks.Add(function (data) {
         data.math = data.math.replace(/^(\/\/\s*)?<!\[CDATA\[|(\/\/\s*)?\]\]>$/g, '');
         data.math = data.math.replace("% <![CDATA[",""); 
          console.log(data.math);
       });
     });
     </script>
```

- update link color: _variable.scss ($link-color  )
