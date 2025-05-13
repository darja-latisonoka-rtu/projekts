### Projekta uzdevuma apraksts

Šis projekts ir vienkārša tīmekļa lietotne, kas ļauj lietotājam pievienot, skatīt, kārtot, rediģēt un dzēst uzdevumus. Lietotne ir izstrādāta ar Python programmēšanas valodu un Flask ietvaru, un dati tiek glabāti JSON failā

Mērķis: izstrādāt uzdevumu pārvaldības lietotni, kurā lietotājs var:

* pievienot jaunu uzdevumu ar termiņu un prioritāti
* skatīt visus uzdevumus
* kārtot uzdevumus pēc termiņa vai prioritātes
* dzēst konkrētus uzdevumus
* rediģēt esošos uzdevumus

---

### Izmantotās Python bibliotēkas un to izvēles pamatojums

* Flask – izmantots kā viegls tīmekļa ietvars, kas ļauj ātri izveidot serveri un maršrutus HTML lapām
* json – datu glabāšanai izmantojam JSON formātu, jo tas ir vienkāršs un piemērots maziem projektiem
* os — pārbauda vai tasks.json fails eksistē
* datetime — potenciāli var tikt izmantots termiņu validācijai vai salīdzināšanai

---

### Izstrādes laikā definētās datu struktūras

Uzdevumi tiek glabāti kā saraksts ar vārdnīcām. Katram uzdevumam ir šādi lauki:

{
    "id": 1,
    "title": "Uzdevuma nosaukums",
    "deadline": "2025-05-10",
    "priority": "vidējs"
}

* `id` – unikāls uzdevuma identifikators
* `title` – uzdevuma nosaukums
* `deadline` – izpildes termiņš (formāts: YYYY-MM-DD)
* `priority` – prioritāte (vērtības: zems, vidējs, augsts)

---

### Maršruti (Routes)
`/` Galvenā lapa. Rāda visus uzdevumus ar kārtošanas iespējām 
`/add` Apstrādā  pieprasījumu, lai pievienotu jaunu uzdevumu                  
`/delete/<task_id>` Dzēš uzdevumu pēc ID un pārrēķina ID secību
`/edit/<task_id>` Parāda rediģēšanas formu. Saglabā labojumus konkrētam uzdevumam

---

### Funkcionalitāte

* `load_tasks()` – Ielādē datus no JSON faila
* `save_tasks(tasks)` – Saglabā datus JSON failā
* `index()` – Rāda visus uzdevumus, atbalsta kārtošanu
* `add_task()` – Pievieno jaunu uzdevumu
* `delete_task(task_id)` – Noņem konkrētu uzdevumu
* `edit_task(task_id)` – Rediģē esošu uzdevumu

---

### HTML un CSS

* `templates/index.html` – Galvenā lapa ar uzdevumu pievienošanu, sarakstu un kārtošanu
* `templates/edit.html` – Forma, lai rediģētu konkrētu uzdevumu
* `static/style.css` – Moderns un responsīvs dizains ar krāsu kodēšanu atbilstoši prioritātei (zaļš = zems, oranžs = vidējs, sarkans = augsts)
* Atbalsta arī mobilās ierīces ar elastīgu izkārtojumu