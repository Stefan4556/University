#include "GUI.h"
#include "Clasa_cu_observer.h"

void GUI::initGUIDesg(){

    QPalette pal = palette();
    pal.setColor(QPalette::Window, Qt::green);
    setPalette(pal);

    QHBoxLayout* coloane = new QHBoxLayout();

    setLayout(coloane);

    ////////////////////////////////////////// ne ocupam de partea stanga
    QWidget* coloana1 = new QWidget;
    QFormLayout* linii1 = new QFormLayout;
    coloana1->setLayout(linii1);

    // text box
    //lista_filme = new QListWidget;
    //linii1->addWidget(lista_filme);
    list_view = new QListView;
    list_view->setUniformItemSizes(true);
    list_model = new MyListModel(srv.get_all());       // modificare 1
    list_view->setModel(list_model);
    linii1->addWidget(list_view);

    // buton afiseaza
    afiseaza = new QPushButton("&Afiseaza");
    linii1->addWidget(afiseaza);

    // cerinta lab - afiseaza tabel
    afiseaza_tabel = new QPushButton("&Afiseaza tabel");
    linii1->addWidget(afiseaza_tabel);

    // rand 1 de butoane
    QWidget* lin_st_butoane1 = new QWidget;
    QHBoxLayout* lay_st_1 = new QHBoxLayout();
    lin_st_butoane1->setLayout(lay_st_1);

    // buton sortare titlu
    sortare_titlu = new QPushButton("&SortByTitlu");
    lay_st_1->addWidget(sortare_titlu);

    // buton sortare actor
    sortare_actor = new QPushButton("&SortByActor");
    lay_st_1->addWidget(sortare_actor);

    // butone sortare an si gen
    sortare_an_gen = new QPushButton("&SortByAnSiGen");
    lay_st_1->addWidget(sortare_an_gen);

    linii1->addWidget(lin_st_butoane1);

    // rand 2 de butoane
    QWidget* lin_st_butoane2 = new QWidget;
    QHBoxLayout* lay_st_2 = new QHBoxLayout();
    lin_st_butoane2->setLayout(lay_st_2);

    // buton spre filtru titlu
    filtru_titlu = new QPushButton("&FilterByTitlu");
    lay_st_2->addWidget(filtru_titlu);

    // buton spre filtru an
    filtru_an = new QPushButton("&FilterByAn");
    lay_st_2->addWidget(filtru_an);

    // buton spre raport
    raport = new QPushButton("&Raport");
    lay_st_2->addWidget(raport);

    linii1->addWidget(lin_st_butoane2);

    // buton spre exit
    exit = new QPushButton("&Exit");
    //QPalette paletaExit = exit->palette();
    //paletaExit.setColor(QPalette::Button, Qt::red);
    //exit->setAutoFillBackground(true);
    //exit->setPalette(paletaExit);
    //exit->update();
    exit->setStyleSheet("background-color:red");
    linii1->addWidget(exit);

    ////////////////////////////////////////// ne ocupam de partea dreapta
    QWidget *coloana2 = new QWidget;
    QFormLayout* linii2 = new QFormLayout;
    coloana2->setLayout(linii2);

    // id
    QLabel* ID = new QLabel("Id");
    txtID = new QLineEdit;
    linii2->addRow(ID, txtID);

    // titlu
    QLabel* TITLU = new QLabel("Titlu");
    txtTITLU = new QLineEdit;
    linii2->addRow(TITLU, txtTITLU);

    // gen
    QLabel* GEN = new QLabel("Gen");
    txtGEN = new QLineEdit;
    linii2->addRow(GEN, txtGEN);

    // an
    QLabel* AN = new QLabel("An");
    txtAN = new QLineEdit;
    linii2->addRow(AN, txtAN);

    // actor
    QLabel* ACTOR = new QLabel("Actor principal");
    txtACTOR = new QLineEdit;
    linii2->addRow(ACTOR, txtACTOR);
    //QWidget* dreapta = new QWidget;

   QLabel* RAND = new QLabel("");
   linii2->addRow(RAND);

    coloane->addWidget(coloana2);

    // Rand 1 de butoane
    QWidget* lin_1_butoane = new QWidget;
    QHBoxLayout* lay1 = new QHBoxLayout();
    lin_1_butoane->setLayout(lay1);

    // buton adauga
    adauga = new QPushButton("&Adauga");
    lay1->addWidget(adauga);

    // buton sterge
    sterge = new QPushButton("&Sterge");
    lay1->addWidget(sterge);

    // buton cauta
    cauta = new QPushButton("&Cauta");
    lay1->addWidget(cauta);

    // buton undo
    undo = new QPushButton("&Undo");
    lay1->addWidget(undo);

    linii2->addRow(lin_1_butoane);

    // Rand 2 de butoane
    QWidget* lin_2_butoane = new QWidget;
    QHBoxLayout* lay2 = new QHBoxLayout();
    lin_2_butoane->setLayout(lay2);

    // buton modifica titlu
    modifica_titlu = new QPushButton("&Modifica titlu");
    lay2->addWidget(modifica_titlu);

    // buton modifica gen
    modifica_gen = new QPushButton("&Modifica gen");
    lay2->addWidget(modifica_gen);

    // buton modifica an
    modifica_an = new QPushButton("&Modifica an");
    lay2->addWidget(modifica_an);

    // buton modifica actor
    modifica_actor = new QPushButton("&Modifica actor");
    lay2->addWidget(modifica_actor);

    linii2->addRow(lin_2_butoane);

    // partea de cos

    // titlu
    QLabel* TITLU_COS = new QLabel("Titlu film");
    txtTITLU_COS = new QLineEdit;
    linii2->addRow(TITLU_COS, txtTITLU_COS);

    // numar filme
    QLabel* NUMAR = new QLabel("Numar filme");
    txtNUMAR = new QLineEdit;
    linii2->addRow(NUMAR, txtNUMAR);

    // fisier export
    QLabel* FISIER = new QLabel("Nume fisier");
    txtFISIER = new QLineEdit;
    linii2->addRow(FISIER, txtFISIER);

    // ad gen gol
    QWidget* lin_3_butoane = new QWidget;
    QHBoxLayout* lay3 = new QHBoxLayout();
    lin_3_butoane->setLayout(lay3);

    // buton adauga cos
    adauga_cos = new QPushButton("&Adauga film");
    lay3->addWidget(adauga_cos);

    // buton genereaza
    genereaza_cos = new QPushButton("&Genereaza filme");
    lay3->addWidget(genereaza_cos);

    // buton goleste
    golire_cos = new QPushButton("&Goleste cos");
    lay3->addWidget(golire_cos);

    linii2->addWidget(lin_3_butoane);

    // exp afis
    QWidget* lin_4_butoane = new QWidget;
    QHBoxLayout* lay4 = new QHBoxLayout();
    lin_4_butoane->setLayout(lay4);

    // buton exporta cos
    export_fis = new QPushButton("&Export");
    lay4->addWidget(export_fis);

    // buton afisare cos
    afisare_cos = new QPushButton("&Afisare cos");
    lay4->addWidget(afisare_cos);

    linii2->addWidget(lin_4_butoane);

    QWidget* lin_5_butoane = new QWidget;
    QHBoxLayout* lay5 = new QHBoxLayout();
    CosCRUDGUI = new QPushButton("CosCRUDGUI");
    CosReadOnlyGUI = new QPushButton("CosReadOnlyGUI");
    lay5->addWidget(CosCRUDGUI);
    lay5->addWidget(CosReadOnlyGUI);
    lin_5_butoane->setLayout(lay5);
    linii2->addWidget(lin_5_butoane);

    coloane->addWidget(coloana1);
    coloane->addWidget(coloana2);

}

void GUI::connectButtons() {

    connect(adauga, &QPushButton::clicked, this, &GUI::adauga_film);
    connect(afiseaza, &QPushButton::clicked, this, &GUI::afisare_filme);
    connect(sterge, &QPushButton::clicked, this, &GUI::sterge_film);
    connect(cauta, &QPushButton::clicked, this, &GUI::cauta_film);
    connect(modifica_titlu, &QPushButton::clicked, this, &GUI::modifica_titlu_film);
    connect(modifica_gen, &QPushButton::clicked, this, &GUI::modifica_gen_film);
    connect(modifica_an, &QPushButton::clicked, this, &GUI::modifica_an_film);
    connect(modifica_actor, &QPushButton::clicked, this, &GUI::modifica_actor_film);
    connect(undo, &QPushButton::clicked, this, &GUI::undo_film);
    connect(filtru_titlu, &QPushButton::clicked, this, &GUI::filterbytitle);
    connect(filtru_an, &QPushButton::clicked, this, &GUI::filterbyan);
    connect(raport, &QPushButton::clicked, this, &GUI::raport_filme);
    connect(adauga_cos, &QPushButton::clicked, this, &GUI::adauga_film_cos);
    connect(genereaza_cos, &QPushButton::clicked, this, &GUI::adauga_film_cos_random);
    connect(golire_cos, &QPushButton::clicked, this, &GUI::goleste_cos);
    connect(afisare_cos, &QPushButton::clicked, this, &GUI::afiseaza_filme_cos);
    connect(export_fis, &QPushButton::clicked, this, &GUI::exporta_cos);
    connect(sortare_titlu, &QPushButton::clicked, this, &GUI::sortare_filme_titlu);
    connect(sortare_actor, &QPushButton::clicked, this, &GUI::sortare_filme_actor);
    connect(sortare_an_gen, &QPushButton::clicked, this, &GUI::sortare_filme_an_gen);
    connect(afiseaza_tabel, &QPushButton::clicked, this, &GUI::afisare_filme_tabel);
    //connect(lista_filme, &QListWidget::itemClicked, this, &GUI::afisare_obiect_selectat);//trb conectata lista
    connect(list_view->selectionModel(), &QItemSelectionModel::selectionChanged, this, [&]() {

        if (list_view->selectionModel()->selectedIndexes().isEmpty())

            return;

        auto ind = list_view->selectionModel()->selectedIndexes().at(0);

        QString date = ind.data(Qt::DisplayRole).toString();

        QStringList lis_date = date.split(" ");

        int id = lis_date[1].toInt();

        Film f = this->srv.get_item_by_id(id);

        string id_s = std::to_string(f.get_id());
        string titlu_s = f.get_titlu();
        string gen_s = f.get_gen();
        string an_s = std::to_string(f.get_an_aparitie());
        string actor_s = f.get_actor_principal();

        txtID->setText(QString::fromStdString(id_s));
        txtTITLU->setText(QString::fromStdString(titlu_s));
        txtGEN->setText(QString::fromStdString(gen_s));
        txtAN->setText(QString::fromStdString(an_s));
        txtACTOR->setText(QString::fromStdString(actor_s));
    });
    connect(CosCRUDGUI, &QPushButton::clicked, this, &GUI::CosCRUDGUI_functie);
    connect(CosReadOnlyGUI, &QPushButton::clicked, this, &GUI::CosReadOnlyGUI_functie);
    connect(exit, SIGNAL(clicked()), qApp, SLOT(quit()));
}
/*
void GUI::loadFilmeIntoList(const vector<Film>& filme) {

    lista_filme->clear();

    for (const auto& f : filme) {

        string id_s = std::to_string(f.get_id());
        string an_s = std::to_string(f.get_an_aparitie());
        auto text = QString::fromStdString("Id: " + id_s + " Titlu: " + f.get_titlu() + " Gen: " + f.get_gen() + " An: " + an_s + " Actor: " + f.get_actor_principal());
        QListWidgetItem* item = new QListWidgetItem{ text };
        //item->setBackground(Qt::blue);
        lista_filme->addItem(item);
    }
    QPalette pal3 = palette();
    pal3.setColor(QPalette::Base, Qt::blue);
    lista_filme->setPalette(pal3);
    lista_filme->update();
}*/
/*
void GUI::loadFilmeIntoList(const vector<Film>& filme) {

    for (const auto& f : filme) {

        string id_s = std::to_string(f.get_id());
        string an_s = std::to_string(f.get_an_aparitie());
        auto text = QString::fromStdString("Id: " + id_s + " Titlu: " + f.get_titlu() + " Gen: " + f.get_gen() + " An: " + an_s + " Actor: " + f.get_actor_principal());
        QListWidgetItem* item = new QListWidgetItem(text);
        
    }
}*/

void GUI::setInitialGUIState() {

    //loadFilmeIntoList(srv.get_all());
    //list_model->setFilme(srv.get_all());
    //int nr_filme = srv.numar_filme_cos();
    //string nr_f = std::to_string(nr_filme);
    //txtNUMAR->setText(QString::fromStdString(nr_f));
}

void GUI::afisare_filme() {

    list_model->setFilme(srv.get_all());
}

void GUI::adauga_film() {

    QString id_qs = txtID->text();
    QString titlu_qs = txtTITLU->text();
    QString gen_qs = txtGEN->text();
    QString an_qs = txtAN->text();
    QString actor_qs = txtACTOR->text();

    txtID->clear();
    txtTITLU->clear();
    txtGEN->clear();
    txtAN->clear();
    txtACTOR->clear();

    //int id = std::stoi(id_qs.toStdString());
    int id = id_qs.toInt();
    string titlu = titlu_qs.toStdString();
    string gen = gen_qs.toStdString();
    //int an = std::stoi(an_qs.toStdString());
    int an = an_qs.toInt();
    string actor = actor_qs.toStdString();

    try {

        srv.adauga_film(id, titlu, gen, an, actor);
        list_model->setFilme(srv.get_all());
        table_model->setFilme(srv.get_all());
    }
    catch (const ValidationError& err){

        QString eroare = QString::fromStdString(err.getMessage());
        QMessageBox::warning(nullptr,"Validation Error",eroare);
    }
    catch (const RepoError& err) {

        QString eroare = QString::fromStdString(err.getMessage());
        QMessageBox::warning(nullptr, "Repository Error", eroare);
    }
}

void GUI::sterge_film() {

    QString id_qs = txtID->text();
    txtID->clear();
    //int id = std::stoi(id_qs.toStdString());
    int id = id_qs.toInt();
    try {

        srv.sterge_film(id);
        list_model->setFilme(srv.get_all());
    }
    catch (const ValidationError& err) {

        QString eroare = QString::fromStdString(err.getMessage());
        QMessageBox::warning(nullptr, "Validation Error", eroare);
    }
    catch (const RepoError& err) {

        QString eroare = QString::fromStdString(err.getMessage());
        QMessageBox::warning(nullptr, "Repository Error", eroare);
    }
}

void GUI::cauta_film() {

    QString id_qs = txtID->text();
    txtID->clear();
    //int id = std::stoi(id_qs.toStdString());
    int id = id_qs.toInt();
    try {

        srv.cauta_film(id);
        const Film& f = srv.get_item_by_id(id);
        string film = "Id: " + std::to_string(f.get_id()) + " Titlu: " + f.get_titlu() + " Gen: " + f.get_gen() + " An: " + std::to_string(f.get_an_aparitie()) + " Actor: " + f.get_actor_principal();
        QMessageBox::information(nullptr,"Filmul a fost gasit!",QString::fromStdString(film));
    }
    catch (const ValidationError& err) {

        QString eroare = QString::fromStdString(err.getMessage());
        QMessageBox::warning(nullptr, "Validation Error", eroare);
    }
    catch (const SrvError& err) {

        QString eroare = QString::fromStdString(err.getMessage());
        QMessageBox::warning(nullptr, "Service Error", eroare);
    }
}

void GUI::modifica_titlu_film() {

    QString id_qs = txtID->text();
    QString titlu_qs = txtTITLU->text();

    txtID->clear();
    txtTITLU->clear();

    //int id = std::stoi(id_qs.toStdString());
    int id = id_qs.toInt();
    string titlu = titlu_qs.toStdString();

    try {

        srv.modifica_titlu_film(id,titlu);
        list_model->setFilme(srv.get_all());
    }
    catch (const ValidationError& err) {

        QString eroare = QString::fromStdString(err.getMessage());
        QMessageBox::warning(nullptr, "Validation Error", eroare);
    }
    catch (const RepoError& err) {

        QString eroare = QString::fromStdString(err.getMessage());
        QMessageBox::warning(nullptr, "Repository Error", eroare);
    }
}

void GUI::modifica_gen_film() {

    QString id_qs = txtID->text();
    QString gen_qs = txtGEN->text();

    txtID->clear();
    txtGEN->clear();

    //int id = std::stoi(id_qs.toStdString());
    int id = id_qs.toInt();
    string gen = gen_qs.toStdString();

    try {

        srv.modifica_gen_film(id, gen);
        list_model->setFilme(srv.get_all());
    }
    catch (const ValidationError& err) {

        QString eroare = QString::fromStdString(err.getMessage());
        QMessageBox::warning(nullptr, "Validation Error", eroare);
    }
    catch (const RepoError& err) {

        QString eroare = QString::fromStdString(err.getMessage());
        QMessageBox::warning(nullptr, "Repository Error", eroare);
    }
}

void GUI::modifica_an_film() {

    QString id_qs = txtID->text();
    QString an_qs = txtAN->text();

    txtID->clear();
    txtAN->clear();

    //int id = std::stoi(id_qs.toStdString());
    int id = id_qs.toInt();
    //int an = std::stoi(an_qs.toStdString());
    int an = an_qs.toInt();

    try {

        srv.modifica_anul_film(id, an);
        list_model->setFilme(srv.get_all());
    }
    catch (const ValidationError& err) {

        QString eroare = QString::fromStdString(err.getMessage());
        QMessageBox::warning(nullptr, "Validation Error", eroare);
    }
    catch (const RepoError& err) {

        QString eroare = QString::fromStdString(err.getMessage());
        QMessageBox::warning(nullptr, "Repository Error", eroare);
    }
}

void GUI::modifica_actor_film() {

    QString id_qs = txtID->text();
    QString actor_qs = txtACTOR->text();

    txtID->clear();
    txtACTOR->clear();

    //int id = std::stoi(id_qs.toStdString());
    int id = id_qs.toInt();
    string actor = actor_qs.toStdString();

    try {

        srv.modifica_actor_film(id, actor);
        list_model->setFilme(srv.get_all());
    }
    catch (const ValidationError& err) {

        QString eroare = QString::fromStdString(err.getMessage());
        QMessageBox::warning(nullptr, "Validation Error", eroare);
    }
    catch (const RepoError& err) {

        QString eroare = QString::fromStdString(err.getMessage());
        QMessageBox::warning(nullptr, "Repository Error", eroare);
    }
}

void GUI::undo_film() {

    try {

        srv.undo();
        list_model->setFilme(srv.get_all());
    }
    catch (const SrvError& err) {

        QString eroare = QString::fromStdString(err.getMessage());
        QMessageBox::warning(nullptr, "Service Error", eroare);
    }
}

void GUI::filterbytitle() {

    QString titlu_qs = txtTITLU->text();

    txtTITLU->clear();

    string titlu = titlu_qs.toStdString();

    vector<Film> lista_filtrata = srv.filtrare_titlu(titlu);
    list_model->setFilme(lista_filtrata);
}

void GUI::filterbyan() {

    QString an_qs = txtAN->text();

    txtAN->clear();

    //int an = std::stoi(an_qs.toStdString());
    int an = an_qs.toInt();

    vector<Film> lista_filtrata = srv.filtrare_an(an);
    list_model->setFilme(lista_filtrata);
}

void GUI::raport_filme() {

    map<string, int> rez = srv.raport();
    string text = "";
    for (const auto& el : rez) {

        text += "Genul: ";
        text += el.first;
        text += " Numar de filme: ";
        text += std::to_string(el.second);
        text += "\n";
    }
    QMessageBox::information(nullptr, "Raport", QString::fromStdString(text));
}

void GUI::adauga_film_cos() {

    QString titlu_qs = txtTITLU_COS->text();

    txtTITLU_COS->clear();

    string titlu = titlu_qs.toStdString();

    try {

        srv.adauga_in_cos(titlu);
        int nr_filme = srv.numar_filme_cos();
        string nr_f = std::to_string(nr_filme);
        //txtNUMAR->setText(QString::fromStdString(nr_f));
    }
    catch (const RepoError& err) {

        QString eroare = QString::fromStdString(err.getMessage());
        QMessageBox::warning(nullptr, "Repository Error", eroare);
    }
}

void GUI::adauga_film_cos_random() {

    QString numar_qs = txtNUMAR->text();

    int nr_filme = srv.numar_filme_cos();
    string nr_f = std::to_string(nr_filme);
    txtNUMAR->setText(QString::fromStdString(nr_f));

    string numar_s = numar_qs.toStdString();

    int nr = std::stoi(numar_s);

    try {

        srv.adauga_random_cos(nr);
        nr_filme = srv.numar_filme_cos();
        nr_f = std::to_string(nr_filme);
        //txtNUMAR->setText(QString::fromStdString(nr_f));
        txtNUMAR->clear();
    }
    catch (const CosError& err) {

        QString eroare = QString::fromStdString(err.getMessage());
        QMessageBox::warning(nullptr, "Cos Error", eroare);
    }

}

void GUI::goleste_cos() {

    srv.goleste_cos();
    //txtNUMAR->setText("0");
}

void GUI::afiseaza_filme_cos() {

    vector<Film> cos = srv.get_cos_filme();
    string text = "";
    for (const auto& f : cos) {

        text += "Id: ";
        text += std::to_string(f.get_id());
        text += " Titlu: ";
        text += f.get_titlu();
        text += " Gen: ";
        text += f.get_gen();
        text += " An: ";
        text += std::to_string(f.get_an_aparitie());
        text += " Actor: ";
        text += f.get_actor_principal();
        text += "\n";
    }

    if (text == "")

        text = "Cosul de filme este gol!";

    QMessageBox::information(nullptr, "Cos", QString::fromStdString(text));
}

void GUI::exporta_cos() {

    QString fisier_qs = txtFISIER->text();
    txtFISIER->clear();

    string fisier = fisier_qs.toStdString();
    try {

        srv.exporta_fisier(fisier);
    }
    catch (const CosError& err) {

        QString eroare = QString::fromStdString(err.getMessage());
        QMessageBox::warning(nullptr, "Cos Error", eroare);
    }
}

void GUI::sortare_filme_titlu() {

    QMessageBox msgBox;
    msgBox.setText("Cum doriti sa sortati filmele dupa titlu?");
    QPushButton* crescButton = msgBox.addButton("Crescator", QMessageBox::ActionRole);
    QPushButton* descrescButton = msgBox.addButton("Descrescator", QMessageBox::ActionRole);

    msgBox.exec();

    vector<Film> rez;

    if (msgBox.clickedButton() == crescButton) {
        
        rez = srv.sortare_filme("titlu","crescator");
    }
    else if (msgBox.clickedButton() == descrescButton) {
        
        rez = srv.sortare_filme("titlu", "descrescator");
    }

    list_model->setFilme(rez);
}

void GUI::sortare_filme_actor() {

    QMessageBox msgBox;
    msgBox.setText("Cum doriti sa sortati filmele dupa actor?");
    QPushButton* crescButton = msgBox.addButton("Crescator", QMessageBox::ActionRole);
    QPushButton* descrescButton = msgBox.addButton("Descrescator", QMessageBox::ActionRole);

    msgBox.exec();

    vector<Film> rez;

    if (msgBox.clickedButton() == crescButton) {

        rez = srv.sortare_filme("actor", "crescator");
    }
    else if (msgBox.clickedButton() == descrescButton) {

        rez = srv.sortare_filme("actor", "descrescator");
    }

    list_model->setFilme(rez);
}

void GUI::sortare_filme_an_gen() {

    QMessageBox msgBox;
    msgBox.setText("Cum doriti sa sortati filmele dupa an si gen?");
    QPushButton* crescButton = msgBox.addButton("Crescator", QMessageBox::ActionRole);
    QPushButton* descrescButton = msgBox.addButton("Descrescator", QMessageBox::ActionRole);

    msgBox.exec();

    vector<Film> rez;

    if (msgBox.clickedButton() == crescButton) {

        rez = srv.sortare_filme("an si gen", "crescator");
    }
    else if (msgBox.clickedButton() == descrescButton) {

        rez = srv.sortare_filme("an si gen", "descrescator");
    }

    list_model->setFilme(rez);
}
/*
void GUI::afisare_filme_tabel() {

    vector<Film> lista = srv.get_all();

    int lung_lista = static_cast<int>(lista.size());

    QTableWidget* tabel = new QTableWidget(lung_lista, 5);

    //QPalette pal1 = palette();
    //pal1.setColor(QPalette::Base, Qt::magenta);
    //tabel->setPalette(pal1);
    //tabel->update();

    int i = 0;

    for (const auto& f : lista) {

        string id_s = std::to_string(f.get_id());
        string an_s = std::to_string(f.get_an_aparitie());
        QTableWidgetItem* obj = new QTableWidgetItem(QString::fromStdString(id_s));
        obj->setBackground(Qt::magenta);
        tabel->setItem(i, 0, obj);

        QTableWidgetItem* obj1 = new QTableWidgetItem(QString::fromStdString(f.get_titlu()));
        obj1->setBackground(Qt::magenta);
        tabel->setItem(i, 1, obj1);

        QTableWidgetItem* obj2 = new QTableWidgetItem(QString::fromStdString(f.get_gen()));
        obj2->setBackground(Qt::magenta);
        tabel->setItem(i, 2, obj2);

        QTableWidgetItem* obj3 = new QTableWidgetItem(QString::fromStdString(an_s));
        obj3->setBackground(Qt::magenta);
        tabel->setItem(i, 3, obj3);

        QTableWidgetItem* obj4 = new QTableWidgetItem(QString::fromStdString(f.get_actor_principal()));
        obj4->setBackground(Qt::magenta);
        tabel->setItem(i, 4, obj4);
        i++;
    }

    tabel->show();
}*/

void GUI::afisare_filme_tabel() {

    table_view = new QTableView;

    table_model = new MyTableModel(this->srv.get_all());

    table_view->setModel(table_model);

    table_view->show();
}

void GUI::afisare_obiect_selectat() {

    auto el = lista_filme->currentItem()->text();

    QStringList lista_filme_split = el.split(" ");

    QString element = lista_filme_split[1];

    Film f = this->srv.get_item_by_id(element.toInt());

    string id_s = std::to_string(f.get_id());
    string titlu_s = f.get_titlu();
    string gen_s = f.get_gen();
    string an_s = std::to_string(f.get_an_aparitie());
    string actor_s = f.get_actor_principal();

    txtID->setText(QString::fromStdString(id_s));
    txtTITLU->setText(QString::fromStdString(titlu_s));
    txtGEN->setText(QString::fromStdString(gen_s));
    txtAN->setText(QString::fromStdString(an_s));
    txtACTOR->setText(QString::fromStdString(actor_s));
}

void GUI::CosCRUDGUI_functie(){

    CosCRUDGUI_Window* win1 = new CosCRUDGUI_Window(this->srv.getCos());

    win1->show();
}

void GUI::CosReadOnlyGUI_functie(){

    CosReadOnlyGUI_Window* win2 = new CosReadOnlyGUI_Window(this->srv.getCos());

    win2->show();
}

