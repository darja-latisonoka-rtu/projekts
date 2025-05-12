### Projekta uzdevuma apraksts

Šis projekts ir vienkārša tīmekļa lietotne, kas ļauj lietotājam pievienot, skatīt, kārtot un dzēst uzdevumus. Lietotne ir izstrādāta ar Python programmēšanas valodu un Flask ietvaru, un dati tiek glabāti JSON failā

Mērķis: izstrādāt uzdevumu pārvaldības lietotni, kurā lietotājs var:

* pievienot jaunu uzdevumu ar termiņu un prioritāti
* skatīt visus uzdevumus tabulas veidā
* kārtot uzdevumus pēc termiņa vai prioritātes
* dzēst konkrētus uzdevumus

---

### Izmantotās Python bibliotēkas un to izvēles pamatojums

* Flask – izmantots kā viegls tīmekļa ietvars, kas ļauj ātri izveidot serveri un maršrutus HTML lapām
* json – datu glabāšanai izmantojam JSON formātu, jo tas ir vienkāršs un piemērots maziem projektiem
* os — pārbauda vai tasks.json fails eksistē
* datetime — potenciāli var tikt izmantots termiņu validācijai vai salīdzināšanai

---

### Izstrādes laikā definētās datu struktūras

Uzdevumi tiek glabāti kā saraksts ar vārdnīcām. Katram uzdevumam ir šādi lauki:

* id – unikāls uzdevuma identifikators
* title – uzdevuma nosaukums 
* deadline – izpildes termiņš (YYYY-MM-DD)
* priority – prioritāte (zems, vidējs, augsts)

Piemērs:
{
    "id": 1,
    "title": "Uzdevuma nosaukums",
    "deadline": "2025-05-10",
    "priority": "vidējs"
}

---

### Tīmekļa lapas (maršruti):

/ – Galvenā lapa. Rāda visus uzdevumus un ļauj tos kārtot
/add – Pieņem POST pieprasījumu, lai pievienotu jaunu uzdevumu
/delete/<task_id> – Dzēš uzdevumu ar konkrēto ID

### Papildfunkcijas:

Uzdevumu sarakstu var kārtot pēc termiņa vai prioritātes
Pēc dzēšanas tiek pārrēķināti uzdevumu ID, lai tie saglabātu secību

### Funkcijas

load_tasks() – Ielādē uzdevumus no JSON faila
save_tasks(tasks) – Saglabā izmaiņas JSON failā
index() – Galvenais skatījums, kurā attēloti uzdevumi un kārtošanas funkcionalitāte
add_task() – Apstrādā formu, lai pievienotu jaunu uzdevumu
delete_task(task_id) – Noņem uzdevumu pēc ID                 

HTML veidne atrodas `templates/index.html` un CSS stili ir `static/style.css` failā