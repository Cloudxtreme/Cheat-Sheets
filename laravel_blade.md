User content: ```{{{ $text }}}```
Raw text: ```@{{ $text }}```
Not escaped data: ```{{ $text }}```

### Conditionals ###
```
@if (count($records) === 1)
    I have one record!
@elseif (count($records) > 1)
    I have multiple records!
@else
    I don't have any records!
@endif

@unless (Auth::check())
    You are not signed in.
@endunless
```

### Loops ###
```
@for ($i = 0; $i < 10; $i++)
    The current value is {{ $i }}
@endfor

@foreach ($users as $user)
    <p>This is user {{ $user->id }}</p>
@endforeach

@forelse($users as $user)
      <li>{{ $user->name }}</li>
@empty
      <p>No users</p>
@endforelse

@while (true)
    <p>I'm looping forever.</p>
@endwhile
```

### Includes ###
Inclide view: ```@include('view.name', array('some'=>'data'))```
Append Sections: ```@section('my.content') .. @stop```
Overwriting Sections: ```@section('my.content') .. @overwrite```
