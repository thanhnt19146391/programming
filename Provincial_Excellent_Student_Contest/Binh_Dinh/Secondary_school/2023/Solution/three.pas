program Solve;
uses math, sysutils;

var
  a, count, pos: array of Integer;
  res: string;
  i, j, subtask, n, k: Integer;
  s: string;

procedure QuickSort(var a: array of Char; left, right: Integer);
var
  i, j, pivot: Integer;
  temp: Char;
begin
  if left < right then
  begin
    pivot := left;
    i := left;
    j := right;
    while i < j do
    begin
      while (a[i] <= a[pivot]) and (i < right) do
        i := i + 1;
      while a[j] > a[pivot] do
        j := j - 1;
      if i < j then
      begin
        temp := a[i];
        a[i] := a[j];
        a[j] := temp;
      end;
    end;
    temp := a[pivot];
    a[pivot] := a[j];
    a[j] := temp;
    QuickSort(a, left, j - 1);
    QuickSort(a, j + 1, right);
  end;
end;

procedure Solve;
var
  i: Integer;
begin
  SetLength(a, Length(s));
  for i := 1 to Length(s) do
    a[i-1] := Ord(s[i]);
  QuickSort(a, 0, Length(a) - 1);

  i := 0;
  while i < Length(a) do
  begin
    j := i;
    while (j + 1 < Length(a)) and (a[i] = a[j+1]) do
      j := j + 1;
    SetLength(pos, Length(pos) + 1);
    pos[Length(pos)-1] := i;
    SetLength(count, Length(count) + 1);
    count[Length(count)-1] := j - i + 1;
    i := j + 1;
  end;

  if Length(pos) = 1 then 
    subtask := 0
  else 
    subtask := 1;

  res := '';

  if subtask = 0 then
  begin
    for i := 1 to Ceil(n / k) do
      res := res + Char(a[0]);
  end;

  if subtask = 1 then
  begin
    if count[0] < k then
      res := res + Char(a[k-1])
    else
    begin
      if count[0] > k then
      begin
        for i := 1 to count[0] - k do
          res := res + Char(a[0]);
        for i := pos[1] to Length(a) - 1 do
          res := res + Char(a[i]);
      end
      else  // count[0] = k;
      begin
        res := res + Char(a[0]);
        i := 0;
        while (i + 1 < Length(count)) do
        begin
          i := i + 1;
          if count[i] mod k = 0 then
            for j := 1 to count[i] div k do
              res := res + Char(a[pos[i]])
          else
          begin
            for j := pos[i] to Length(a) - 1 do
              res := res + Char(a[j]);
            break;
          end;
        end;
      end;
    end;

    WriteLn(res);
  end;
end;

begin
  ReadLn(n, k);
  ReadLn(s);
  Solve;
end."
