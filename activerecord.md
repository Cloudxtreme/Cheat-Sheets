```
Person.where(name: 'Spartacus', rating: 4) # returns list (maybe empty)
Person.find_by(name: 'Spartacus', rating: 4) # the first item or nil.
Person.where(name: 'Spartacus', rating: 4).first_or_initialize
Person.where(name: 'Spartacus', rating: 4).first_or_create

Person.where(..).exists?(conditions = :none)
Person.where(..).ids
Person.where(..).pluck(:field1, :field2) # just these fields

```