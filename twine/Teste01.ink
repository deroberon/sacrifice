VAR variable1 = 0

-> twine.Start


=== twine===
= Start
~variable1 = 0
What is happening here?
* [label2] ->twine.label2
* [label3] ->twine.label3


= label2
~variable1 = variable1+1
Somei um
* [label4] ->twine.label4

= label3
Vamos para o 4
* [label4] ->twine.label4
* [label5] ->twine.label5

= label4
* {variable1 == 1}  [label5] ->twine.label5
->END

= label5
Double-click this passage to edit it.
->END

