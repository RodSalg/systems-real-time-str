with Ada.Text_IO; use Ada.Text_IO;

-- aqui vou sempre definir as variáveis
procedure INVERTER_STRING is

    text : String (1 .. 15);
    invertido : String (1 .. 15);
    text_lenght : Integer;

begin
    Put("digite o palindromo: ");
    Get_Line(text, text_lenght);
    original: String := text(1 .. text_lenght);

    begin
        -- percorre do último até o primeiro caractere
        for I in 1 .. text_lenght loop
            invertido(I) := original(text_lenght - I + 1);
        end loop;

        Put_Line("string oroginal: " & text(1 .. text_lenght));
        Put_Line("string inversa: " & invertido(1 .. text_lenght));

        if original = invertido(1 .. text_lenght) then
            Put_Line("É um palíndromo!");
        else
            Put_Line("Não é um palíndromo.");
        end if;
    end;

end INVERTER_STRING;
