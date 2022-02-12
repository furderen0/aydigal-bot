from mailbox import Message
import discord
from discord.ext import commands
import requests
import typing
import os
from discord.utils import get
import sys
import shutil
import random
import cryptocompare
import datetime
import psutil
from bs4 import BeautifulSoup
import platform

client = commands.Bot(command_prefix="?")

@client.command()
async def kriptopara(ctx):
    kripto = discord.Embed(title="Kripto Para Fiyatları:", color=0x03ff00)
    kriptoParaBTC = cryptocompare.get_avg("BTC", "USD")
    BTCfiyat = kriptoParaBTC["PRICE"]
    BTCdusuk = kriptoParaBTC["LOW24HOUR"]
    BTCyuksek = kriptoParaBTC["HIGH24HOUR"]
    kriptoParaETH = cryptocompare.get_avg("ETH", "USD")
    ETHfiyat = kriptoParaETH["PRICE"]
    ETHdusuk = kriptoParaETH["LOW24HOUR"]
    ETHyuksek = kriptoParaETH["HIGH24HOUR"]
    kriptoParaXRP = cryptocompare.get_avg("XRP", "USD")
    XRPfiyat = kriptoParaXRP["PRICE"]
    XRPdusuk = kriptoParaXRP["LOW24HOUR"]
    XRPyuksek = kriptoParaXRP["HIGH24HOUR"]
    kriptoParaBNB = cryptocompare.get_avg("BNB", "USD")
    BNBfiyat = kriptoParaBNB["PRICE"]
    BNBdusuk = kriptoParaBNB["LOW24HOUR"]
    BNByuksek = kriptoParaBNB["HIGH24HOUR"]
    kriptoParaSOL = cryptocompare.get_avg("SOL", "USD")
    SOLfiyat = kriptoParaSOL["PRICE"]
    SOLdusuk = kriptoParaSOL["LOW24HOUR"]
    SOLyuksek = kriptoParaSOL["HIGH24HOUR"]
    kriptoParaADA = cryptocompare.get_avg("ADA", "USD")
    ADAfiyat = kriptoParaADA["PRICE"]
    ADAdusuk = kriptoParaADA["LOW24HOUR"]
    ADAyuksek = kriptoParaADA["HIGH24HOUR"]
    kriptoParaDOT = cryptocompare.get_avg("DOT", "USD")
    DOTfiyat = kriptoParaDOT["PRICE"]
    DOTdusuk = kriptoParaDOT["LOW24HOUR"]
    DOTyuksek = kriptoParaDOT["HIGH24HOUR"]
    kriptoParaDOGE = cryptocompare.get_avg("DOGE", "USD")
    DOGEfiyat = kriptoParaDOGE["PRICE"]
    DOGEdusuk = kriptoParaDOGE["LOW24HOUR"]
    DOGEyuksek = kriptoParaDOGE["HIGH24HOUR"]
    kriptoParaMATIC = cryptocompare.get_avg("MATIC", "USD")
    MATICfiyat = kriptoParaMATIC["PRICE"]
    MATICdusuk = kriptoParaMATIC["LOW24HOUR"]
    MATICyuksek = kriptoParaMATIC["HIGH24HOUR"]
    kripto.add_field(name="**Bitcoin**", value=f"Fiyatı: {BTCfiyat}$\n 24 Saatin En Yükseği: {BTCyuksek}$\n24 Saatin En Düşüğü: {BTCdusuk}$", inline=True)
    kripto.add_field(name="**Ethereum**", value=f"Fiyatı: {ETHfiyat}$\n 24 Saatin En Yükseği: {ETHyuksek}$\n24 Saatin En Düşüğü: {ETHdusuk}$", inline=True)
    kripto.add_field(name="**Ripple**", value=f"Fiyatı: {XRPfiyat}$\n 24 Saatin En Yükseği: {XRPyuksek}$\n24 Saatin En Düşüğü: {XRPdusuk}$", inline=True)
    kripto.add_field(name="**Binance Coin**", value=f"Fiyatı: {BNBfiyat}$\n 24 Saatin En Yükseği: {BNByuksek}$\n24 Saatin En Düşüğü: {BNBdusuk}$", inline=True)
    kripto.add_field(name="**Solana**", value=f"Fiyatı: {SOLfiyat}$\n 24 Saatin En Yükseği: {SOLyuksek}$\n24 Saatin En Düşüğü: {SOLdusuk}$", inline=True)
    kripto.add_field(name="**Cardano**", value=f"Fiyatı: {ADAfiyat}$\n 24 Saatin En Yükseği: {ADAyuksek}$\n24 Saatin En Düşüğü: {ADAdusuk}$", inline=True)
    kripto.add_field(name="**Doge**", value=f"Fiyatı: {DOGEfiyat}$\n 24 Saatin En Yükseği: {DOGEyuksek}$\n24 Saatin En Düşüğü: {DOGEdusuk}$", inline=True)
    kripto.add_field(name="**Polkadot**", value=f"Fiyatı: {DOTfiyat}$\n 24 Saatin En Yükseği: {DOTyuksek}$\n24 Saatin En Düşüğü: {DOTdusuk}$", inline=True)
    kripto.add_field(name="**Polygon**", value=f"Fiyatı: {MATICfiyat}$\n 24 Saatin En Yükseği: {MATICyuksek}$\n24 Saatin En Düşüğü: {MATICdusuk}$", inline=True)
    await ctx.reply(embed=kripto)

@client.command()
async def changemymind(ctx, *, text:str):
    apiurl =  f"https://nekobot.xyz/api/imagegen?type=changemymind&text={text}"
    req = requests.get(apiurl)
    jsonolsn = req.json()
    changemymindEmbed = discord.Embed()
    changemymindEmbed.set_image(url=jsonolsn["message"])
    await ctx.reply(embed=changemymindEmbed)

@client.command()
async def avatar(ctx, *, member: discord.Member = None):
    if member == None:
        member = ctx.author
    avatarEmbed = discord.Embed(title="Profil Fotoğrafı:", description=f"[.png olarak indir]({member.avatar_url_as(format='png', size=1024)}) | [.jpg olarak indir]({member.avatar_url_as(format='jpg', size=1024)}) | [.webp olarak indir]({member.avatar_url_as(format='webp', size=1024)})")
    avatarEmbed.set_image(url=member.avatar_url)
    await ctx.reply(embed=avatarEmbed)

@client.command()
async def trumptweet(ctx, *, text:str):
    link = f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}"
    istekatrump = requests.get(link)
    jsonolmasn = istekatrump.json()
    trumpEmbed = discord.Embed()
    trumpEmbed.set_image(url=jsonolmasn["message"])
    await ctx.reply(embed=trumpEmbed)

@client.command()
async def tweet(ctx, *, text:str):
    link = f"https://nekobot.xyz/api/imagegen?type=tweet&username={ctx.author.name}&text={text}"    
    req_at = requests.get(link)
    jsonehe = req_at.json()
    tweet = discord.Embed()
    tweet.set_image(url=jsonehe["message"])
    await ctx.reply(embed=tweet)

@client.command()
async def kur(ctx):
    try:
        Currency = requests.get('http://bigpara.hurriyet.com.tr/doviz/')
        BSoup = BeautifulSoup(Currency.content,'html.parser')
        ForeignCur = BSoup.find_all("span",{"class" :"value"})

        USD = ForeignCur[2].text.replace(",",".")
        EUR = ForeignCur[5].text.replace(",",".")
        GBP = ForeignCur[8].text.replace(",",".")

        USDPer=ForeignCur[0].text
        EURPer=ForeignCur[3].text
        GBPPer=ForeignCur[6].text

        if USDPer.startswith('-') == False:
            USDPer = f"+{USDPer}"

        if EURPer.startswith('-') == False:
            EURPer = f"+{EURPer}"

        if GBPPer.startswith('-') == False:
            GBPPer = f"+{GBPPer}"

        exUSD=round(1/float(USD),4)
        exEUR=round(1/float(EUR),4)
        exGBP=round(1/float(GBP),4)

        currencyEmbed = discord.Embed(title="Canlı Döviz Kuru",colour = 0x36393F,timestamp = ctx.message.created_at)
        currencyEmbed.add_field(name=f":flag_us:    {USDPer}",value = f'1 $ = **{USD}** ₺\n1 ₺ = **{exUSD}** $')
        currencyEmbed.add_field(name=f":flag_eu:    {EURPer}",value = f'1 € = **{EUR}** ₺\n1 ₺ = **{exEUR}** €')
        currencyEmbed.add_field(name=f":flag_gb:    {GBPPer}",value = f'1 £ = **{GBP}** ₺\n1 ₺ = **{exGBP}** £')
        currencyEmbed.set_footer(text=f"Tarafından: {ctx.author}",icon_url=ctx.author.avatar_url)

        await ctx.send(embed=currencyEmbed)
    except Exception as e:
        currencyEmbed_2 = discord.Embed(title="Hata",description =f"{e}",colour = 0xd92929)
        await ctx.send(embed=currencyEmbed_2)

@client.command()
async def ping(ctx):
    pingEmbed = discord.Embed(description=f"**Pingim {round(client.latency*1000)}ms**")
    await ctx.reply(embed=pingEmbed)

@client.command(description="Bot istatistikleri.", aliases=["stats"], guild_only=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def istatistik(ctx):
    dpy_version = discord.version_info
    formatted_version = f"{dpy_version.major}.{dpy_version.minor}.{dpy_version.micro}"

    embed = discord.Embed()
    embed.title = f"{client.user.name} için Bilgiler"
    embed.add_field(name="Python", value=f":snake: **Python Versiyonu**: {platform.python_version()}\n:package: **Discord.py Versiyonu**: {formatted_version}", inline=False)
    embed.add_field(name="Bot", value=f":speech_balloon: **Kanal Sayısı**: {len([i for i in client.get_all_channels()])}\n:white_check_mark: **Sunucu Sayısı**: {len(client.guilds)}\n:bust_in_silhouette: **Toplam Üye Sayısı**: {len([i for i in client.get_all_members()])}", inline=False)
    embed.add_field(name="Sunucu", value=f":desktop: **İşletim Sistemi**: {platform.platform()}\n:mag: **Bellek Boyutu**: {psutil.virtual_memory().total >> 20}\n:mag: **İşlemci Modeli**: {platform.processor()}", inline=False)
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.reply(embed=embed)

@client.command()
async def userinfo(ctx, member: typing.Optional[discord.Member]):
    if member == None:
        member = ctx.author

    if member.bot:
        kullanıcı_botmu = "Evet"
    else:
        kullanıcı_botmu = "Hayır"

    kullanıcı_id = member.id

    kullanici_rolleri_list = [r.mention for r in member.roles if r != ctx.guild.default_role]
    kullanici_butun_roller_fix = ", ".join(kullanici_rolleri_list)

    kullanici_sunucuya_giris_obj = str(member.joined_at)
    kullanici_bolunmus_sunucuya_giris = kullanici_sunucuya_giris_obj.split(".")
    kullanici_sunucuya_giris = kullanici_bolunmus_sunucuya_giris[0]

    kullanici_hesap_tarihi_obj = str(member.created_at)
    kullanici_bolunmus_hesap_tarihi = kullanici_hesap_tarihi_obj.split(".")
    kullanici_hesap_tarihi = kullanici_bolunmus_hesap_tarihi[0]
    renk = kullanici_rolleri_list[0].replace('<@&', '').replace('>','')

    userinfoembed = discord.Embed(title="Bilgiler:", description=f"<@{kullanıcı_id}>")
    userinfoembed.add_field(name="Kullanıcı ID:", value=member.display_name)
    userinfoembed.add_field(name="ID:", value=f"{kullanıcı_id}")
    userinfoembed.add_field(name="Bot mu?", value=f"{kullanıcı_botmu}")
    userinfoembed.add_field(name=f"Rolleri {len(kullanici_rolleri_list)}", value=f"{kullanici_butun_roller_fix}")
    userinfoembed.add_field(name="Avatar Linki:", value=f"[Tıkla]({member.avatar_url})")
    userinfoembed.add_field(name="Hesap oluşturulma tarihi:", value=f"{kullanici_hesap_tarihi}")
    userinfoembed.add_field(name="Sunucuya giriş tarihi:", value=f"{kullanici_sunucuya_giris}")
    userinfoembed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=userinfoembed)

@client.command()
async def sosyalmedya(ctx):
    sosyalmedya = discord.Embed(description="<:YouTube:882946871256043550> [Aydigal YT](https://www.youtube.com/channel/UC8MIZXQTUZlq3_q7HXRoq-g)\n<:instagram:882946470033096724>  [Aydigal Instagram]( https://www.instagram.com/aydigal/)\n<:Twitter:882946871130218516> [Aydigal Twitter](https://twitter.com/aydigal11)\n<:SpotifyLogo:882946873164455976> [Aydigal Spotify](https://open.spotify.com/user/i67c9eztghxmf461eayrc4k1a)\n<:steam:882946871134404618> [Aydigal Steam](https://steamcommunity.com/id/aydinigalgezer)", color=0xFF0000)
    await ctx.reply(embed=sosyalmedya)

@client.command()
async def kutuac(ctx):
    rastgelesayi = random.randint(0,101)
    print(rastgelesayi)
    if rastgelesayi < 51:
        rareitem = open(r'rare.txt').readlines()
        rareitemm = random.choice(rareitem)
        bolRare = rareitemm.split('|')
        response = requests.get(bolRare[2])
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        tr = soup.find("tr", {"id": "matrixRow0"})
        td = tr.find_all("td")
        fiyat = td[1].text
        if fiyat == "":
            fiyat.replace("", "Fiyat bulunamadı")
        kutuEmbed = discord.Embed(title="**Kutu açıldı:**", color=0x277ECD)
        kutuEmbed.add_field(name="Çıkan item:", value=bolRare[0])
        kutuEmbed.add_field(name="Değeri (Kredi):", value=fiyat)
        kutuEmbed.add_field(name="Rengi:", value=bolRare[3])
        kutuEmbed.add_field(name="Nadirliği:", value="Rare")
        kutuEmbed.set_image(url=bolRare[1])
        kutuEmbed.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.reply(embed=kutuEmbed)
    if rastgelesayi > 50:
        if rastgelesayi < 71:
            rareitem = open(r'veryrare.txt').readlines()
            rareitemm = random.choice(rareitem)
            bolRare = rareitemm.split('|')
            response = requests.get(bolRare[2])
            html = response.text
            soup = BeautifulSoup(html, "html.parser")
            tr = soup.find("tr", {"id": "matrixRow0"})
            td = tr.find_all("td")
            fiyat = td[1].text
            if fiyat == "":
                fiyat.replace("", "Fiyat bulunamadı")
            kutuEmbed = discord.Embed(title="**Kutu açıldı:**", color=0x931CD1)
            kutuEmbed.add_field(name="Çıkan item:", value=bolRare[0])
            kutuEmbed.add_field(name="Değeri (Kredi):", value=fiyat)
            kutuEmbed.add_field(name="Rengi:", value=bolRare[3])
            kutuEmbed.add_field(name="Nadirliği:", value="Very Rare")
            kutuEmbed.set_image(url=bolRare[1])
            kutuEmbed.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.reply(embed=kutuEmbed)
    if rastgelesayi > 70:
        if rastgelesayi < 86:
            rareitem = open(r'import.txt').readlines()
            rareitemm = random.choice(rareitem)
            bolRare = rareitemm.split('|')
            response = requests.get(bolRare[2])
            html = response.text
            soup = BeautifulSoup(html, "html.parser")
            tr = soup.find("tr", {"id": "matrixRow0"})
            td = tr.find_all("td")
            fiyat = td[1].text
            if fiyat == "":
                fiyat.replace("", "Fiyat bulunamadı")
            kutuEmbed = discord.Embed(title="**Kutu açıldı:**", color=0xFF0000)
            kutuEmbed.add_field(name="Çıkan item:", value=bolRare[0])
            kutuEmbed.add_field(name="Değeri (Kredi):", value=fiyat)
            kutuEmbed.add_field(name="Rengi:", value=bolRare[3])
            kutuEmbed.add_field(name="Nadirliği:", value="İmport")
            kutuEmbed.set_image(url=bolRare[1])
            kutuEmbed.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.reply(embed=kutuEmbed)
        if rastgelesayi > 85:
            if rastgelesayi < 95:
                rareitem = open(r'exotic.txt').readlines()
                rareitemm = random.choice(rareitem)
                bolRare = rareitemm.split('|')
                response = requests.get(bolRare[2])
                html = response.text
                soup = BeautifulSoup(html, "html.parser")
                tr = soup.find("tr", {"id": "matrixRow0"})
                td = tr.find_all("td")
                fiyat = td[1].text
                if fiyat == "":
                    fiyat.replace("", "Fiyat bulunamadı")
                kutuEmbed = discord.Embed(title="**Kutu açıldı:**", color=0xE4DA0E)
                kutuEmbed.add_field(name="Çıkan item:", value=bolRare[0])
                kutuEmbed.add_field(name="Değeri (Kredi):", value=fiyat)
                kutuEmbed.add_field(name="Rengi:", value=bolRare[3])
                kutuEmbed.add_field(name="Nadirliği:", value="Exotic")
                kutuEmbed.set_image(url=bolRare[1])
                kutuEmbed.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
                await ctx.reply(embed=kutuEmbed)
        if rastgelesayi > 95:
            if rastgelesayi < 100:
                rareitem = open(r'blackmarket.txt').readlines()
                rareitemm = random.choice(rareitem)
                bolRare = rareitemm.split('|')
                response = requests.get(bolRare[2])
                html = response.text
                soup = BeautifulSoup(html, "html.parser")
                tr = soup.find("tr", {"id": "matrixRow0"})
                td = tr.find_all("td")
                fiyat = td[1].text
                if fiyat == "":
                    fiyat.replace("", "Fiyat bulunamadı")
                kutuEmbed = discord.Embed(title="**Kutu açıldı:**", color=0xC401FF)
                kutuEmbed.add_field(name="Çıkan item:", value=bolRare[0])
                kutuEmbed.add_field(name="Değeri (Kredi):", value=fiyat)
                kutuEmbed.add_field(name="Rengi:", value=bolRare[3])
                kutuEmbed.add_field(name="Nadirliği:", value="Black Market")
                kutuEmbed.set_image(url=bolRare[1])
            kutuEmbed.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.reply(embed=kutuEmbed)
    if rastgelesayi == 100:
        rareitem = open(r'alpha.txt').readlines()
        rareitemm = random.choice(rareitem)
        bolRare = rareitemm.split('|')
        response = requests.get(bolRare[2])
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        tr = soup.find("tr", {"id": "matrixRow0"})
        td = tr.find_all("td")
        fiyat = td[1].text
        if fiyat == "":
            fiyat.replace("", "Fiyat bulunamadı")
        kutuEmbed = discord.Embed(title="**Kutu açıldı:**", color=0xEFFF01)
        kutuEmbed.add_field(name="Çıkan item:", value=bolRare[0])
        kutuEmbed.add_field(name="Değeri (Kredi):", value=fiyat)
        kutuEmbed.add_field(name="Rengi:", value=bolRare[3])
        kutuEmbed.add_field(name="Nadirliği:", value="Alpha İtemi (Limited)")
        kutuEmbed.set_image(url=bolRare[1])
        kutuEmbed.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.reply(embed=kutuEmbed)




client.run(token)
