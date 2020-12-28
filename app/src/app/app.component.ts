import { Component, OnInit, ViewChild } from '@angular/core';
import { UtilsService } from './utils.service';
import { WebService } from './web.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'app';

  imagenes = []

  constructor(private service: WebService, private utils: UtilsService) { }

  async ngOnInit(): Promise<void> {

  }

  onUploadChange(event: any) {
    if(!event.srcElement.files[0].name.endsWith(".jpg")){
      (<HTMLInputElement>document.getElementById(`imagen`)).value = ""
      this.utils.mostrarError('Archivo invalido. Debe ser .jpg!')
      return
    }

    const file = event.target.files[0];
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => {
        this.imagenes.push(reader.result.toString())
    };
    (<HTMLInputElement>document.getElementById(`imagen`)).value = ""
  }
}
