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
  [ref](https://groups.google.com/forum/#!topic/mathjax-users/AS6swTZzyWY)
add _inclue/footer/custom.html
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

- fix mermaid cannot render
  [ref](https://github.com/mermaid-js/mermaid/issues/772)
add _inclue/footer/custom.html
```javascript
<script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/8.0.0/mermaid.min.js"></script>
<script>
var config = {
    startOnLoad:true,
    theme: 'forest',
    flowchart:{
            useMaxWidth:false,
            htmlLabels:true
        }
};
mermaid.initialize(config);
window.mermaid.init(undefined, document.querySelectorAll('.language-mermaid'));
</script>

```

- update link color: _variable.scss ($link-color  )
