# highlighting_tool
Script to add HTML tags to a text to highlight specific characters in boldfont.

Tags can be added in two ways: 
* highlight characters in the middle of words
* highlight characters at the end of words


# Examples:
“Viva Garibaldi!” sang a young Italian boy in an uptown street. He held a battered violin
that looked as if it had been used for generations.

* mark middle:

“V<b>iv</b>a Gar<b>iba</b>ldi!” s<b>an</b>g <b>a</b> y<b>ou</b>ng It<b>al</b>ian b<b>o</b>y i<b>n</b> a<b>n</b> up<b>to</b>wn st<b>re</b>et. H<b>e</b> h<b>el</b>d <b>a</b> bat<b>ter</b>ed vi<b>ol</b>in t<b>ha</b>t lo<b>ok</b>ed a<b>s</b> i<b>f</b> i<b>t</b> h<b>a</b>d b<b>ee</b>n u<b>se</b>d f<b>o</b>r gen<b>erat</b>ions.
```sh
“V<b>iv</b>a Gar<b>iba</b>ldi!” s<b>an</b>g <b>a</b> y<b>ou</b>ng It<b>al</b>ian b<b>o</b>y i<b>n</b> a<b>n</b> up<b>to</b>wn st<b>re</b>et. H<b>e</b> h<b>el</b>d <b>a</b> bat<b>ter</b>ed vi<b>ol</b>in t<b>ha</b>t lo<b>ok</b>ed a<b>s</b> i<b>f</b> i<b>t</b> h<b>a</b>d b<b>ee</b>n u<b>se</b>d f<b>o</b>r gen<b>erat</b>ions. 
```

* mark end:

“Vi<b>va</b> Gariba<b>ldi</b>!” sa<b>ng</b> <b>a</b> you<b>ng</b> Itali<b>an</b> bo<b>y</b> i<b>n</b> a<b>n</b> upto<b>wn</b> stre<b>et</b>. H<b>e</b> he<b>ld</b> <b>a</b> batte<b>red</b> viol<b>in</b> th<b>at</b> look<b>ed</b> a<b>s</b> i<b>f</b> i<b>t</b> ha<b>d</b> be<b>en</b> us<b>ed</b> fo<b>r</b> generat<b>ions</b>. 
```sh
“Vi<b>va</b> Gariba<b>ldi</b>!” sa<b>ng</b> <b>a</b> you<b>ng</b> Itali<b>an</b> bo<b>y</b> i<b>n</b> a<b>n</b> upto<b>wn</b> stre<b>et</b>. H<b>e</b> he<b>ld</b> <b>a</b> batte<b>red</b> viol<b>in</b> th<b>at</b> look<b>ed</b> a<b>s</b> i<b>f</b> i<b>t</b> ha<b>d</b> be<b>en</b> us<b>ed</b> fo<b>r</b> generat<b>ions</b>. 
```
## Additional functionality:
### Split text
Texts can be converted into a list of their sentences:

"Hello World. I am a text. Just a simple text." 
```sh
['Hello World.', 'I am a text.', 'Just a simple text.']
```
Or a string with a separator (fe. "|") separating the sentences:

"Hello World. I am a text. Just a simple text." 
```sh
'Hello World. | I am a text. | Just a simple text.'
```

### BBCode to HTML
Texts marked with BBCode tags will be stripped from tags that do not indicate boldfont and boldfont markings will be turned into HTML tags.
```sh
[FONT=Liberation Serif]This is [B]another[/B] example text. It is [B]marked[/B] with BBCode tags.[/FONT]
```
```sh
This is <b>another</b> example text. It is <b>marked</b> with BBCode tags.
```
