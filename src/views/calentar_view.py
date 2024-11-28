import discord
from src.Github_api_manager.github_api import GithubApi
class InputDate(discord.ui.Modal, title="Date"):
    def __init__(self):
        super().__init__()


        # Crear el campo de entrada dentro del constructor
        self.input_field = discord.ui.TextInput(
            label='Ambiente',
            placeholder="Leones",
            style=discord.TextStyle.short,  # Campo de texto corto
            required=True,
            min_length=5,
            default=''
        )
        self.input_field_1 = discord.ui.TextInput(
            label="Dia",
            placeholder="Ejemplo '22'",
            style=discord.TextStyle.short,  # Campo de texto corto
            required=True,
            min_length=2,
            default=''
        )
        self.input_field_2 = discord.ui.TextInput(
            label='Mes',
            placeholder="Ejemplo '02'",
            style=discord.TextStyle.short,  # Campo de texto corto
            required=True,
            min_length=2,
            default=''
        )
        self.input_field_3 = discord.ui.TextInput(
            label="Año",
            placeholder="Ejemplo '2021'",
            style=discord.TextStyle.short,  # Campo de texto corto
            required=True,
            min_length=4,
            default=''
        )
        self.add_item(self.input_field)
        self.add_item(self.input_field_1)
        self.add_item(self.input_field_2)  # Añadir el campo al modal
        self.add_item(self.input_field_3)

    async def on_submit(self, interaction: discord.Interaction):
        #await interaction.message.delete()

        env = self.input_field.value.strip()
        # foramt -date="2024-11-21"
        date = f"{self.input_field_3.value}-{self.input_field_2.value}-{self.input_field_1.value}"

        print('::> ', env, date)
        self.github_api = GithubApi(env=self.input_field_1.value)
        self.github_api.get_history(env, date)

        embed = discord.Embed(title=f"Hola {interaction.user.name}!, recibí tu petición.",
                            description=f"Buscando en los datos de **{env}** el **{date}**",
                            colour=discord.Colour.brand_green(),
                            type='article')

        await interaction.response.send_message(embed=embed)
