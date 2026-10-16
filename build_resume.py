from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from pypdf import PdfReader
import pypdfium2 as pdfium
import shutil

out = Path('output/pdf'); out.mkdir(parents=True, exist_ok=True)
preview = Path('tmp/pdfs'); preview.mkdir(parents=True, exist_ok=True)
path = out / 'Arafat-Mughal-Resume-2026.pdf'
blue = HexColor('#2e48ed')
styles = {
 'name': ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=27, leading=32, textColor=HexColor('#20221f'), spaceAfter=4),
 'role': ParagraphStyle('role', fontName='Helvetica', fontSize=13, leading=18, textColor=blue, spaceAfter=10),
 'contact': ParagraphStyle('contact', fontName='Helvetica', fontSize=9, leading=14, textColor=HexColor('#4b514b'), spaceAfter=3),
 'section': ParagraphStyle('section', fontName='Helvetica-Bold', fontSize=10, leading=14, textColor=blue, spaceBefore=14, spaceAfter=7),
 'title': ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=10.5, leading=14, spaceBefore=7, spaceAfter=3),
 'body': ParagraphStyle('body', fontName='Helvetica', fontSize=9.6, leading=14, textColor=HexColor('#303630'), spaceAfter=5),
 'bullet': ParagraphStyle('bullet', fontName='Helvetica', fontSize=9.6, leading=14, textColor=HexColor('#303630'), leftIndent=10, firstLineIndent=-8, spaceAfter=4),
}
story=[]
def p(text, style='body'): story.append(Paragraph(text, styles[style]))
def bullet(text): p('- '+text, 'bullet')
def section(text): p(text.upper(), 'section')
def link(url, label): return f'<link href="{url}" color="#2e48ed">{label}</link>'
def footer(c, doc):
 c.setStrokeColor(HexColor('#dce0d3')); c.line(44, 40, A4[0]-44, 40)
 c.setFont('Helvetica',8); c.setFillColor(HexColor('#64695f'))
 c.drawString(44,27,'Arafat Mughal | Full-Stack Developer')
 c.drawRightString(A4[0]-44,27,f'{doc.page} / 2')

p('ARAFAT MUGHAL','name')
p('Full-Stack Developer','role')
p('Lahore, Pakistan  |  +92 313 2555703  |  '+link('mailto:arfat.bjs@gmail.com','arfat.bjs@gmail.com'),'contact')
p(link('https://arfat-mughal.github.io/','Portfolio')+'  |  '+link('https://github.com/Arfat-Mughal','GitHub')+'  |  '+link('https://www.linkedin.com/in/arafat-mughal-369434122/','LinkedIn')+'  |  '+link('https://wa.me/923132555703','WhatsApp'),'contact')
section('Profile')
p('Full-stack developer with experience since 2019 building Laravel applications, React interfaces, REST and GraphQL APIs, and business integrations. Recent delivery includes conversational procurement automation, AI-enabled business platforms, and container-based release workflows. Open to full-time opportunities and freelance projects.')
section('Technical skills')
p('<b>Web &amp; APIs:</b> PHP, Laravel, React, Redux, Vue.js, Next.js, REST, GraphQL, Apollo Client, Inertia.js, Livewire, Filament, WordPress, HTML, CSS, Tailwind CSS, Bootstrap, jQuery.')
p('<b>Data &amp; delivery:</b> MySQL, Git, GitHub Actions, Docker, GHCR, nginx, environment separation, health checks, deployment rollback.')
p('<b>AI &amp; integrations:</b> Copilot Studio, Power Automate, Dataverse, Power Apps, Dynamics 365 F&amp;O, Teams, Entra ID, NetSuite, Microsoft Graph / SharePoint, Claude API, payment gateways, social login. Additional experience with AI bots and animation.')
section('Professional experience')
p('Laravel Developer | BJS Softsolution, Lahore','title')
p('July 2019 - Present','contact')
bullet('Build REST and GraphQL APIs and connect Laravel backends to React / Redux and Apollo Client interfaces.')
bullet('Develop web applications, administrative tools, and integrations for payments and social authentication.')
bullet('Deliver procurement workflows, enterprise integrations, and release automation across the projects below.')
section('Recent delivery highlights')
p('Autolus Buying Assistant | Conversational procurement demo','title')
bullet('Delivered a sentence-to-purchase-order workflow using Copilot Studio, Dataverse, Power Automate, Dynamics 365 F&amp;O, Teams, and Power Apps.')
bullet('Connected 28 buying categories to financial coding, rate-card estimates, routing, draft orders, and approval workflows through four automated flows. The end-to-end demo passed 18 of 18 tests.')
p('GenieWorks | AI business platform &amp; deployment automation','title')
bullet('Delivered Laravel and Next.js container releases using GitHub Actions and GHCR, with off-server builds, health checks, deployment locking, backups, and automatic rollback.')
bullet('Created isolated staging with masked data and restricted database access; added encryption-key consistency checks and audited company-level controls for NetSuite posting.')
bullet('Configured environment-specific integrations for a platform supporting AI invoice review, template-based SOW drafting, and SharePoint documents.')

story.append(PageBreak())
p('SELECTED WORK & BACKGROUND','role')
section('Selected projects')
p('Bechly.pk | Marketplace, web &amp; Android | Mar - Jul 2026','title')
p('Classifieds platform connecting a Laravel backend, web experience, and Android app, with location search, moderation, and notifications. Stack: Laravel, Filament, Livewire, REST APIs. '+link('https://bechly.pk','Website')+' | '+link('https://play.google.com/store/apps/details?id=com.bechly.pk','Google Play'))
p('PetCure | Pet-care app, web &amp; Android','title')
p('Medication reminders, health notes, family care, and vet-ready reports. '+link('https://petcure.app','Website')+' | '+link('https://play.google.com/store/apps/details?id=com.petcure.app','Google Play'))
p('The Product Hub (Bring Back Australia) | Nov 2023 - Apr 2024','title')
p('Development contributions using React, Redux, Tailwind CSS, and REST APIs.')
p('Sourcing Genie | Oct 2022 - Oct 2023','title')
p('Contributed to the sourcing platform using React, Redux, Tailwind CSS, and REST APIs.')
p('Procurement League | 2019 - 2022','title')
bullet('Online courses (Aug 2021 - Feb 2022): Laravel GraphQL APIs with React, Redux, and Apollo Client.')
bullet('MRO admin panel (Jan - Jul 2021): Laravel, MySQL, Vue.js, and Inertia.js for Sourcing Genie.')
bullet('Job search portal (2019 - 2020): Laravel, React, GraphQL, MySQL, and Tailwind CSS.')
p('Additional work','title')
p('JSON into TOON converter; BPM Tap Tempo; 5e HP Tracker; AGHS Lahore school management; Al-Falah school CRM; Mega-Crafter; Gurmani Foundation; Rana International Salt; online drug-testing courses.')
section('Earlier experience')
p('Weight Analysis &amp; Reporting | SGI - Specialists Group Inc','title')
p('Oct 2018 - Jan 2019. Analysed delivered material weights, prepared Excel reports, and coordinated customer and banking correspondence.')
p('WordPress &amp; Graphic Design Intern | Creation Next Software House','title')
p('Aug - Dec 2017. Supported WordPress website updates, UI improvements, HTML/CSS/JavaScript development, and graphics for web and social content.')
p('Air Ticketing | Carvan-E-Athhar Travels &amp; Tours','title')
p('Mar 2016 - Jul 2017. Managed reservations, cancellations, schedule changes, and customer communication.')
section('Education & certification')
p('<b>BS Software Engineering</b> | Virtual University of Pakistan | 2014 - 2019<br/><b>Microsoft Office Specialist:</b> Word 2013 (77-418), Certiport')
section('Volunteering & languages')
p('Startup Weekend, LUMS (Aug - Sep 2018). Virtual University activities (2015 - 2018): programming competition, regional quiz, student week, event organisation, e-gaming, and 6th, 8th, and 9th convocations.')
p('<b>Languages:</b> English, Urdu, Punjabi.')
doc=SimpleDocTemplate(str(path),pagesize=A4,rightMargin=44,leftMargin=44,topMargin=36,bottomMargin=52,title='Arafat Mughal - Full-Stack Developer',author='Arafat Mughal')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
reader=PdfReader(str(path))
assert len(reader.pages)==2, f'Unexpected page count: {len(reader.pages)}'
pdf=pdfium.PdfDocument(str(path))
for i,page in enumerate(pdf): page.render(scale=1.3).to_pil().save(preview/f'resume-page-{i+1}.png')
shutil.copyfile(path,'assets/arafat-resume-2026.pdf')
print('Created and rendered two-page resume.')
