import discord
#from src.views.input_mark_view import InputModal
from src.Github_api_manager.github_api import GithubApi
from src.views.multi_embeds import MultiEmbeds

# Vista secundaria para configuraciones
class PerfilSelectView(discord.ui.View):
    def __init__(self, ambiente):
        super().__init__()
        self.ambiente = ambiente
        self.perfil = ''
        self.jira = False


    @discord.ui.button(label="All", style=discord.ButtonStyle.success, custom_id="all")
    async def all(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.perfil = 'Todos'
        mark = 'All'
        jira = 'Si' if self.jira else 'No'

        # EJECUCION
        # github_api_to_all_repo = GithubApi(env=self.ambiente, markers='', jira=self.jira, repo='')
        # github_api_to_all_repo.run_all_tests()

        embed = MultiEmbeds.embed_confirm_auto(interaction,
                                               self.ambiente,
                                               self.perfil,
                                               mark,
                                               jira)

        print('::> ', self.ambiente, ' ::> All  ', 'Jira :>', self.jira)

        await interaction.message.edit(embed=embed, view=None, content=None)

    @discord.ui.button(label="Supervisor", style=discord.ButtonStyle.primary, custom_id="supervisor")
    async def supervisor(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.perfil = 'supervisor'
        modal =  InputModal(self.ambiente, self.perfil, self.jira)
        await interaction.message.edit(embed=modal, view=None, content=None)

    @discord.ui.button(label="Agente", style=discord.ButtonStyle.primary, custom_id="agente")
    async def agente(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.perfil = 'agente'
        modal = InputModal(self.ambiente, self.perfil, self.jira)
        await interaction.response.edit_message(modal)

    @discord.ui.button(label="Bot", style=discord.ButtonStyle.primary, custom_id="bot")
    async def bot(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.perfil = 'bot'
        modal = InputModal(self.ambiente, self.perfil, self.jira)
        await interaction.response.send_modal(modal)

    # "Botón-checkbox" jira
    @discord.ui.button(label="Checkbox: OFF", style=discord.ButtonStyle.secondary, custom_id="checkbox")
    async def checkbox(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Alternar estado del checkbox
        self.jira = not self.jira
        button.label = "Jira rep: ON" if self.jira else "Jira rep: OFF"
        button.style = discord.ButtonStyle.success if self.jira else discord.ButtonStyle.secondary
        print("Estado de JIRA :> ", self.jira)
        await interaction.response.edit_message(view=self)



# Modal para la entrada de datos
class InputModal(discord.ui.Modal):
    def __init__(self, env, perfil, jira):
        super().__init__(title="Input Modal")
        self.env = env
        self.perfil = perfil
        self.jira = jira

        # Agregar un campo de entrada de texto
        self.input = discord.ui.TextInput(label=self.perfil,
            placeholder="Solo escribir en caso de querer ejecutar Marks",
            style=discord.TextStyle.short,  # Campo de texto corto
            required=False,
            min_length=0,
            default='')
        self.add_item(self.input)

    async def on_submit(self, interaction: discord.Interaction):
        # Obtener la entrada del usuario
        print(':::>>> ', self.env, self.perfil, self.input.value, self.jira)

        mark = 'All' if len(self.input.value) == 0 else self.input.value
        jira = 'Si' if self.jira else 'No'

        # EJECUCION
        # github_api_to_all_repo = GithubApi(env=self.env, markers=mark, jira=jira, repo=self.perfil)
        # github_api_to_all_repo.run_tests()

        embed = MultiEmbeds.embed_confirm_auto(interaction,
                                               self.env,
                                               self.perfil,
                                               mark,
                                               jira)
        return embed
        #await interaction.message.edit(embed=embed)