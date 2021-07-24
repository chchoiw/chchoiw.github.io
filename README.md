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
add ```_inclue/footer/custom.html```
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

- update link color: ```/_sass_/_variable.scss ($link-color  )```

- synatax font-size: 
goto the path ```/_sass_/_syntax.scss``` and revise the block to 

```css
  .highlight {
    margin: 0;
    font-family: $monospace;
    font-size: $type-size-5;
    line-height: 1.8;
  }
```

- Add Category ```Notes``` 
  1. Create a folder ```_notes```
  2. add the following code to ```_config.yml``` 
  ```
    notes:
    output: true
    permalink: /:collection/:path/
  ```
  ```
    # _notes
  - scope:
      path: ""
      type: notes
    values:
      layout: single
      author_profile: true
      read_time: true
      comments: true
      share: true
      related: true
  ```
  3. add a new document ```_post/notes.md``` or [download](/post/notes.md) 
  ```markdown
  ---
  layout: archive
  title: "Notes"
  permalink: /notes/
  author_profile: true
  ---

  {% include base_path %}

  {% for post in site.notes reversed %}
    {% include archive-single.html %}
  {% endfor %}
  ```
  4. finally, add ```_data/navigation.yml```
  ```
  - title: "Notes"
    url: /notes/     
  ```