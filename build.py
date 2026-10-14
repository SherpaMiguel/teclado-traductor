# Genera index.html (soporte) y privacy.html en 8 idiomas. Ejecutar: python3 build.py
import html
UPDATED = "2026-10-13"
LANGS = ["es","en","fr","de","it","pt","nl","zh-Hans"]
LABEL = {"es":"Español","en":"English","fr":"Français","de":"Deutsch","it":"Italiano","pt":"Português","nl":"Nederlands","zh-Hans":"简体中文"}
COMPANY = "Sherpas Time Consulting S.L. · B56190440 · Gijón, España"
EMAIL = "soporte@sherpastime.com"

P = {
"es": dict(name="Teclado traductor chat IA", privacy="Política de privacidad", support="Soporte", updated="Última actualización",
 sections=[
 ("Resumen","No tenemos cuentas, servidores ni analítica. Lo que escribes no se guarda ni nos llega. La traducción se hace en tu iPhone o, si tú lo activas, con el proveedor de IA que elijas usando tu propia clave."),
 ("Responsable",f"{COMPANY}. Contacto: {EMAIL}."),
 ("Lo que escribes","El teclado no guarda ni envía lo que escribes. Solo lee el texto de la caja cuando pulsas Traducir, y el mensaje copiado cuando pulsas Pegar."),
 ("Traducción de iOS","Por defecto se usa la traducción integrada de Apple en el propio iPhone: el texto no sale del dispositivo."),
 ("IA opcional","Si activas Claude (Anthropic), Gemini (Google) o ChatGPT (OpenAI) con tu clave, el texto a traducir y los últimos mensajes de la conversación se envían directamente desde tu iPhone a ese proveedor, que los trata según su propia política de privacidad. Nosotros no recibimos nada. La clave se guarda solo en el llavero de tu iPhone."),
 ("Datos en tu iPhone","Para traducir con contexto, el teclado recuerda los últimos mensajes durante 3 horas, solo en tu iPhone. Puedes borrarlos en Ajustes → Olvidar conversación e idioma."),
 ("Plantillas, glosario e iCloud","Tus plantillas y tu glosario se guardan en tu iPhone. Si dejas activado «Sincronizar con iCloud», Apple los copia en tu cuenta de iCloud para llevarlos a tus otros dispositivos. Nosotros no tenemos acceso. Puedes desactivarlo en Ajustes."),
 ("«Permitir acceso total»","iOS lo exige para que el teclado pueda leer el mensaje que copias, conectarse a la IA si la activas y compartir los ajustes con la app. No lo usamos para nada más."),
 ("Suscripción","Las compras y la prueba gratuita las gestiona Apple. No recibimos tus datos de pago."),
 ("Publicidad y rastreo","Sin anuncios, sin rastreo y sin analítica de terceros."),
 ("Tus derechos",f"Como no guardamos datos personales en nuestros sistemas, no hay datos que consultar ni borrar. Para cualquier duda escríbenos a {EMAIL}."),
 ]),
"en": dict(name="AI Chat Translator Keyboard", privacy="Privacy Policy", support="Support", updated="Last updated",
 sections=[
 ("Summary","We have no accounts, servers or analytics. What you type is never stored or sent to us. Translation happens on your iPhone or, if you turn it on, with the AI provider you choose using your own key."),
 ("Controller",f"{COMPANY}. Contact: {EMAIL}."),
 ("What you type","The keyboard doesn’t store or send what you type. It only reads the text box when you tap Translate, and the copied message when you tap Paste."),
 ("iOS translation","By default, Apple’s built-in on-device translation is used: the text never leaves your iPhone."),
 ("Optional AI","If you turn on Claude (Anthropic), Gemini (Google) or ChatGPT (OpenAI) with your own key, the text to translate and the latest messages of the conversation are sent directly from your iPhone to that provider, which handles them under its own privacy policy. We receive nothing. The key is stored only in your iPhone’s keychain."),
 ("Data on your iPhone","To translate with context, the keyboard remembers the latest messages for 3 hours, only on your iPhone. You can delete them in Settings → Forget conversation and language."),
 ("Templates, glossary and iCloud","Your templates and glossary are stored on your iPhone. If “Sync with iCloud” is on, Apple copies them to your iCloud account to bring them to your other devices. We have no access to them. You can turn it off in Settings."),
 ("“Allow Full Access”","iOS requires it so the keyboard can read the message you copy, connect to the AI if you turn it on, and share settings with the app. We don’t use it for anything else."),
 ("Subscription","Purchases and the free trial are handled by Apple. We don’t receive your payment details."),
 ("Ads and tracking","No ads, no tracking and no third-party analytics."),
 ("Your rights",f"Since we don’t keep personal data on our systems, there is no data to access or delete. For any question, write to {EMAIL}."),
 ]),
"fr": dict(name="Clavier traducteur de chat IA", privacy="Politique de confidentialité", support="Assistance", updated="Dernière mise à jour",
 sections=[
 ("En bref","Pas de compte, pas de serveur, pas d’analyse. Ce que vous tapez n’est ni enregistré ni envoyé chez nous. La traduction se fait sur votre iPhone ou, si vous l’activez, avec le fournisseur d’IA de votre choix et votre propre clé."),
 ("Responsable",f"{COMPANY}. Contact : {EMAIL}."),
 ("Ce que vous tapez","Le clavier n’enregistre ni n’envoie ce que vous tapez. Il lit le champ de texte uniquement quand vous touchez Traduire, et le message copié quand vous touchez Coller."),
 ("Traduction iOS","Par défaut, la traduction intégrée d’Apple est utilisée sur l’iPhone : le texte ne quitte pas l’appareil."),
 ("IA en option","Si vous activez Claude (Anthropic), Gemini (Google) ou ChatGPT (OpenAI) avec votre clé, le texte à traduire et les derniers messages de la conversation sont envoyés directement depuis votre iPhone à ce fournisseur, qui les traite selon sa propre politique. Nous ne recevons rien. La clé est stockée uniquement dans le trousseau de votre iPhone."),
 ("Données sur votre iPhone","Pour traduire avec le contexte, le clavier garde les derniers messages pendant 3 heures, uniquement sur votre iPhone. Vous pouvez les effacer dans Réglages → Oublier la conversation et la langue."),
 ("Modèles, glossaire et iCloud","Vos modèles et votre glossaire sont enregistrés sur votre iPhone. Si « Synchroniser avec iCloud » est activé, Apple les copie sur votre compte iCloud pour les retrouver sur vos autres appareils. Nous n’y avons pas accès. Vous pouvez le désactiver dans Réglages."),
 ("« Autoriser l’accès complet »","iOS l’exige pour que le clavier puisse lire le message copié, se connecter à l’IA si vous l’activez et partager les réglages avec l’app. Nous ne l’utilisons pour rien d’autre."),
 ("Abonnement","Les achats et l’essai gratuit sont gérés par Apple. Nous ne recevons pas vos données de paiement."),
 ("Publicité et pistage","Pas de publicité, pas de pistage, pas d’analyse tierce."),
 ("Vos droits",f"Comme nous ne conservons aucune donnée personnelle, il n’y a rien à consulter ni à effacer. Pour toute question : {EMAIL}."),
 ]),
"de": dict(name="KI-Chat-Übersetzer-Tastatur", privacy="Datenschutzerklärung", support="Support", updated="Zuletzt aktualisiert",
 sections=[
 ("Kurz gesagt","Keine Konten, keine Server, keine Analyse. Was du tippst, wird weder gespeichert noch an uns gesendet. Übersetzt wird auf deinem iPhone oder – wenn du es aktivierst – beim KI-Anbieter deiner Wahl mit deinem eigenen Schlüssel."),
 ("Verantwortlicher",f"{COMPANY}. Kontakt: {EMAIL}."),
 ("Was du tippst","Die Tastatur speichert oder sendet nicht, was du tippst. Sie liest das Textfeld nur, wenn du auf Übersetzen tippst, und die kopierte Nachricht nur, wenn du auf Einsetzen tippst."),
 ("iOS-Übersetzung","Standardmäßig wird die integrierte Übersetzung von Apple auf dem iPhone verwendet: Der Text verlässt das Gerät nicht."),
 ("Optionale KI","Wenn du Claude (Anthropic), Gemini (Google) oder ChatGPT (OpenAI) mit deinem Schlüssel aktivierst, werden der zu übersetzende Text und die letzten Nachrichten des Gesprächs direkt von deinem iPhone an diesen Anbieter gesendet, der sie gemäß seiner eigenen Datenschutzerklärung verarbeitet. Wir erhalten nichts. Der Schlüssel wird nur im Schlüsselbund deines iPhones gespeichert."),
 ("Daten auf deinem iPhone","Für Übersetzungen mit Kontext merkt sich die Tastatur die letzten Nachrichten 3 Stunden lang, nur auf deinem iPhone. Du kannst sie unter Einstellungen → Gespräch und Sprache vergessen löschen."),
 ("Vorlagen, Glossar und iCloud","Deine Vorlagen und dein Glossar werden auf deinem iPhone gespeichert. Ist „Mit iCloud synchronisieren“ aktiv, kopiert Apple sie in deinen iCloud-Account, damit sie auf deinen anderen Geräten verfügbar sind. Wir haben keinen Zugriff darauf. Du kannst es in den Einstellungen ausschalten."),
 ("„Vollen Zugriff erlauben“","iOS verlangt dies, damit die Tastatur die kopierte Nachricht lesen, sich bei aktivierter KI verbinden und Einstellungen mit der App teilen kann. Für nichts anderes."),
 ("Abo","Käufe und die Gratis-Testphase werden von Apple abgewickelt. Wir erhalten keine Zahlungsdaten."),
 ("Werbung und Tracking","Keine Werbung, kein Tracking, keine Analyse durch Dritte."),
 ("Deine Rechte",f"Da wir keine personenbezogenen Daten speichern, gibt es nichts einzusehen oder zu löschen. Bei Fragen: {EMAIL}."),
 ]),
"it": dict(name="Tastiera traduttore chat IA", privacy="Informativa sulla privacy", support="Assistenza", updated="Ultimo aggiornamento",
 sections=[
 ("In breve","Nessun account, nessun server, nessuna analisi. Ciò che scrivi non viene salvato né inviato a noi. La traduzione avviene sul tuo iPhone o, se la attivi, con il fornitore di IA che scegli usando la tua chiave."),
 ("Titolare",f"{COMPANY}. Contatto: {EMAIL}."),
 ("Ciò che scrivi","La tastiera non salva né invia ciò che scrivi. Legge il campo di testo solo quando tocchi Traduci, e il messaggio copiato solo quando tocchi Incolla."),
 ("Traduzione di iOS","Per impostazione predefinita si usa la traduzione integrata di Apple sull’iPhone: il testo non lascia il dispositivo."),
 ("IA opzionale","Se attivi Claude (Anthropic), Gemini (Google) o ChatGPT (OpenAI) con la tua chiave, il testo da tradurre e gli ultimi messaggi della conversazione vengono inviati direttamente dal tuo iPhone a quel fornitore, che li tratta secondo la propria informativa. Noi non riceviamo nulla. La chiave è salvata solo nel portachiavi del tuo iPhone."),
 ("Dati sul tuo iPhone","Per tradurre con il contesto, la tastiera ricorda gli ultimi messaggi per 3 ore, solo sul tuo iPhone. Puoi cancellarli in Impostazioni → Dimentica conversazione e lingua."),
 ("Modelli, glossario e iCloud","I tuoi modelli e il tuo glossario sono salvati sull’iPhone. Se «Sincronizza con iCloud» è attivo, Apple li copia nel tuo account iCloud per portarli sugli altri dispositivi. Noi non vi abbiamo accesso. Puoi disattivarlo in Impostazioni."),
 ("«Consenti accesso completo»","iOS lo richiede perché la tastiera possa leggere il messaggio copiato, collegarsi all’IA se la attivi e condividere le impostazioni con l’app. Non lo usiamo per altro."),
 ("Abbonamento","Gli acquisti e la prova gratuita sono gestiti da Apple. Non riceviamo i tuoi dati di pagamento."),
 ("Pubblicità e tracciamento","Nessuna pubblicità, nessun tracciamento, nessuna analisi di terze parti."),
 ("I tuoi diritti",f"Poiché non conserviamo dati personali, non c’è nulla da consultare o cancellare. Per domande: {EMAIL}."),
 ]),
"pt": dict(name="Teclado tradutor de chat IA", privacy="Política de privacidade", support="Suporte", updated="Última atualização",
 sections=[
 ("Resumo","Não temos contas, servidores nem análise. O que escreve não é guardado nem nos é enviado. A tradução é feita no seu iPhone ou, se a ativar, com o fornecedor de IA que escolher usando a sua própria chave."),
 ("Responsável",f"{COMPANY}. Contacto: {EMAIL}."),
 ("O que escreve","O teclado não guarda nem envia o que escreve. Só lê a caixa de texto quando toca em Traduzir, e a mensagem copiada quando toca em Colar."),
 ("Tradução do iOS","Por predefinição é usada a tradução integrada da Apple no próprio iPhone: o texto não sai do dispositivo."),
 ("IA opcional","Se ativar Claude (Anthropic), Gemini (Google) ou ChatGPT (OpenAI) com a sua chave, o texto a traduzir e as últimas mensagens da conversa são enviados diretamente do seu iPhone para esse fornecedor, que os trata segundo a sua própria política. Nós não recebemos nada. A chave fica guardada apenas no porta-chaves do seu iPhone."),
 ("Dados no seu iPhone","Para traduzir com contexto, o teclado lembra as últimas mensagens durante 3 horas, apenas no seu iPhone. Pode apagá-las em Definições → Esquecer conversa e idioma."),
 ("Modelos, glossário e iCloud","Os seus modelos e o seu glossário ficam guardados no iPhone. Se «Sincronizar com o iCloud» estiver ativo, a Apple copia-os para a sua conta iCloud para os levar aos seus outros dispositivos. Nós não temos acesso. Pode desativá-lo nas Definições."),
 ("«Permitir acesso total»","O iOS exige-o para que o teclado possa ler a mensagem copiada, ligar-se à IA se a ativar e partilhar as definições com a app. Não o usamos para mais nada."),
 ("Subscrição","As compras e o período experimental gratuito são geridos pela Apple. Não recebemos os seus dados de pagamento."),
 ("Publicidade e rastreio","Sem anúncios, sem rastreio e sem análise de terceiros."),
 ("Os seus direitos",f"Como não guardamos dados pessoais, não há dados para consultar nem apagar. Para qualquer dúvida: {EMAIL}."),
 ]),
"nl": dict(name="AI-chatvertaaltoetsenbord", privacy="Privacybeleid", support="Ondersteuning", updated="Laatst bijgewerkt",
 sections=[
 ("Samenvatting","Geen accounts, geen servers, geen analyse. Wat je typt wordt niet bewaard en niet naar ons gestuurd. Vertalen gebeurt op je iPhone of, als je dat aanzet, bij de AI-aanbieder van je keuze met je eigen sleutel."),
 ("Verwerkingsverantwoordelijke",f"{COMPANY}. Contact: {EMAIL}."),
 ("Wat je typt","Het toetsenbord bewaart of verstuurt niet wat je typt. Het leest het tekstvak alleen als je op Vertaal tikt, en het gekopieerde bericht alleen als je op Plak tikt."),
 ("iOS-vertaling","Standaard wordt de ingebouwde vertaling van Apple op de iPhone gebruikt: de tekst verlaat het apparaat niet."),
 ("Optionele AI","Als je Claude (Anthropic), Gemini (Google) of ChatGPT (OpenAI) met je eigen sleutel aanzet, worden de te vertalen tekst en de laatste berichten van het gesprek rechtstreeks vanaf je iPhone naar die aanbieder gestuurd, die ze verwerkt volgens zijn eigen privacybeleid. Wij ontvangen niets. De sleutel wordt alleen in de sleutelhanger van je iPhone bewaard."),
 ("Gegevens op je iPhone","Om met context te vertalen onthoudt het toetsenbord de laatste berichten 3 uur lang, alleen op je iPhone. Je kunt ze wissen via Instellingen → Gesprek en taal vergeten."),
 ("Sjablonen, woordenlijst en iCloud","Je sjablonen en woordenlijst worden op je iPhone bewaard. Staat ‘Synchroniseren met iCloud’ aan, dan kopieert Apple ze naar je iCloud-account zodat ze op je andere apparaten komen. Wij hebben er geen toegang toe. Je kunt het uitzetten in Instellingen."),
 ("‘Sta volledige toegang toe’","iOS vereist dit zodat het toetsenbord het gekopieerde bericht kan lezen, verbinding kan maken met de AI als je die aanzet en instellingen kan delen met de app. We gebruiken het nergens anders voor."),
 ("Abonnement","Aankopen en de gratis proefperiode worden door Apple afgehandeld. Wij ontvangen geen betaalgegevens."),
 ("Advertenties en tracking","Geen advertenties, geen tracking en geen analyse door derden."),
 ("Je rechten",f"Omdat we geen persoonsgegevens bewaren, is er niets in te zien of te wissen. Vragen? Mail naar {EMAIL}."),
 ]),
"zh-Hans": dict(name="AI 聊天翻译键盘", privacy="隐私政策", support="支持", updated="最后更新",
 sections=[
 ("概要","我们没有账户、服务器或数据分析。你输入的内容不会被保存，也不会发送给我们。翻译在你的 iPhone 上完成；如你开启，则使用你自己的密钥通过所选 AI 提供商完成。"),
 ("负责人",f"{COMPANY}。联系方式：{EMAIL}。"),
 ("你输入的内容","键盘不会保存或发送你输入的内容。只有在你点按“翻译”时才读取输入框，点按“粘贴”时才读取复制的消息。"),
 ("iOS 翻译","默认使用 Apple 在 iPhone 上的内置翻译：文字不会离开设备。"),
 ("可选 AI","如果你使用自己的密钥开启 Claude（Anthropic）、Gemini（Google）或 ChatGPT（OpenAI），待翻译的文字及最近的对话消息会从你的 iPhone 直接发送给该提供商，并按其隐私政策处理。我们不会收到任何内容。密钥只保存在你 iPhone 的钥匙串中。"),
 ("你 iPhone 上的数据","为结合上下文翻译，键盘会在你的 iPhone 上记住最近的消息 3 小时。你可以在“设置 → 清除对话和语言”中删除。"),
 ("模板、术语表与 iCloud","你的模板和术语表保存在 iPhone 上。如开启“通过 iCloud 同步”，Apple 会将其复制到你的 iCloud 账户，以便在你的其他设备上使用。我们无法访问这些内容。你可以在设置中关闭此项。"),
 ("“允许完全访问”","iOS 要求开启此项，键盘才能读取你复制的消息、在你开启 AI 时联网，并与 App 共享设置。我们不会将其用于其他用途。"),
 ("订阅","购买和免费试用由 Apple 处理。我们不会收到你的付款信息。"),
 ("广告与追踪","无广告、无追踪、无第三方分析。"),
 ("你的权利",f"由于我们不保存个人数据，因此没有可查询或删除的数据。如有疑问，请写信至 {EMAIL}。"),
 ]),
}

S = {
"es": ("Contesta en cualquier idioma sin salir del chat.", ["Instala la app y abre la guía de inicio.","En Ajustes de iOS → Teclados, activa el teclado y «Permitir acceso total».","En cualquier chat, mantén pulsado 🌐 y elige el teclado.","Copia el mensaje recibido para leerlo traducido; escribe en tu idioma y pulsa Traducir."], "¿Necesitas ayuda? Escríbenos a"),
"en": ("Reply in any language without leaving the chat.", ["Install the app and open the getting-started guide.","In iOS Settings → Keyboards, turn on the keyboard and “Allow Full Access”.","In any chat, hold 🌐 and choose the keyboard.","Copy the received message to read it translated; write in your language and tap Translate."], "Need help? Write to"),
"fr": ("Répondez dans n’importe quelle langue sans quitter la conversation.", ["Installez l’app et ouvrez le guide de démarrage.","Dans Réglages iOS → Claviers, activez le clavier et « Autoriser l’accès complet ».","Dans n’importe quelle conversation, maintenez 🌐 et choisissez le clavier.","Copiez le message reçu pour le lire traduit ; écrivez dans votre langue et touchez Traduire."], "Besoin d’aide ? Écrivez à"),
"de": ("Antworte in jeder Sprache, ohne den Chat zu verlassen.", ["Installiere die App und öffne die Einführung.","Aktiviere in den iOS-Einstellungen → Tastaturen die Tastatur und „Vollen Zugriff erlauben“.","Halte in einem beliebigen Chat 🌐 gedrückt und wähle die Tastatur.","Kopiere die empfangene Nachricht, um sie übersetzt zu lesen; schreib in deiner Sprache und tippe auf Übersetzen."], "Brauchst du Hilfe? Schreib an"),
"it": ("Rispondi in qualsiasi lingua senza uscire dalla chat.", ["Installa l’app e apri la guida iniziale.","In Impostazioni iOS → Tastiere, attiva la tastiera e «Consenti accesso completo».","In qualsiasi chat, tieni premuto 🌐 e scegli la tastiera.","Copia il messaggio ricevuto per leggerlo tradotto; scrivi nella tua lingua e tocca Traduci."], "Serve aiuto? Scrivi a"),
"pt": ("Responda em qualquer idioma sem sair do chat.", ["Instale a app e abra o guia de início.","Em Definições do iOS → Teclados, ative o teclado e «Permitir acesso total».","Em qualquer chat, mantenha 🌐 premido e escolha o teclado.","Copie a mensagem recebida para a ler traduzida; escreva no seu idioma e toque em Traduzir."], "Precisa de ajuda? Escreva para"),
"nl": ("Antwoord in elke taal zonder de chat te verlaten.", ["Installeer de app en open de starthandleiding.","Zet in iOS-instellingen → Toetsenborden het toetsenbord en ‘Sta volledige toegang toe’ aan.","Houd in elke chat 🌐 ingedrukt en kies het toetsenbord.","Kopieer het ontvangen bericht om het vertaald te lezen; schrijf in je eigen taal en tik op Vertaal."], "Hulp nodig? Mail naar"),
"zh-Hans": ("无需离开聊天，即可用任何语言回复。", ["安装 App 并打开入门指南。","在 iOS 设置 → 键盘中，开启键盘和“允许完全访问”。","在任意聊天中，按住 🌐 并选择该键盘。","复制收到的消息即可阅读译文；用你的语言书写并点按“翻译”。"], "需要帮助？请写信至"),
}

CSS = """
:root{--bg:#F4F8F7;--card:#ffffff;--ink:#13253A;--mist:#5F6F82;--primary:#0E8F80;--line:#DDE7E5}
@media (prefers-color-scheme:dark){:root{--bg:#0C1620;--card:#13212E;--ink:#EAF1F7;--mist:#9AA9BA;--primary:#2BC4AE;--line:#22323F}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 Manrope,system-ui,sans-serif}
main{max-width:760px;margin:0 auto;padding:32px 16px 64px}header{display:flex;gap:16px;align-items:center;margin-bottom:8px}
header img{width:64px;height:64px;border-radius:15px}h1{font-size:26px;line-height:1.2;margin:0}h2{font-size:18px;margin:28px 0 6px}
nav{display:flex;flex-wrap:wrap;gap:8px;margin:20px 0 8px}nav a{padding:4px 10px;border:1px solid var(--line);border-radius:999px;color:var(--ink);text-decoration:none;font-size:14px}
nav a[aria-current]{background:var(--primary);border-color:var(--primary);color:#fff}a{color:var(--primary)}
section.lang{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:8px 24px 24px;margin-top:20px}
.meta{color:var(--mist);font-size:14px}ol{padding-left:22px}
"""

def page(title, body, active=None):
    nav = "".join(f'<a href="#{l}" lang="{l}">{LABEL[l]}</a>' for l in LANGS)
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;800&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body><main>
<header><img src="icon.png" alt=""><div><h1>{html.escape(title)}</h1><div class="meta">{COMPANY}</div></div></header>
<nav>{nav}</nav>{body}</main></body></html>"""

priv = ""
for l in LANGS:
    p = P[l]
    secs = "".join(f"<h2>{html.escape(t)}</h2><p>{html.escape(x)}</p>" for t, x in p["sections"])
    priv += f'<section class="lang" id="{l}" lang="{l}"><h2>{html.escape(p["name"])} — {html.escape(p["privacy"])}</h2><p class="meta">{p["updated"]}: {UPDATED}</p>{secs}</section>'
open("privacy.html","w").write(page("Teclado traductor chat IA · Privacy", priv))

# Landing multilingüe (raíz en inglés y una carpeta por idioma); incluye la ayuda de soporte.
import landing
landing.build({code: S["zh-Hans" if code == "zh" else code][1] for code in landing.PATHS}, EMAIL)
print("ok")
