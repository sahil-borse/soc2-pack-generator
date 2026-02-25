import { Component, OnInit, signal } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CommonModule } from '@angular/common';
import { DragDropModule, CdkDragDrop, moveItemInArray, transferArrayItem } from '@angular/cdk/drag-drop';

import { BoardConfigService, BoardColumn } from '../../core/services/board-config.service';
import { CompanyControlsService, CompanyControl } from '../../core/services/company-controls.service';

@Component({
  selector: 'app-controls',
  standalone: true,
  imports: [CommonModule, DragDropModule],
  templateUrl: './controls.html'
})
export class ControlsComponent implements OnInit {

  frameworkId!: string;

  columns = signal<BoardColumn[]>([]);
  controls = signal<CompanyControl[]>([]);
  grouped = signal<Record<string, CompanyControl[]>>({});

  constructor(
    private route: ActivatedRoute,
    private boardService: BoardConfigService,
    private controlService: CompanyControlsService
  ) {}

  ngOnInit() {
    this.frameworkId = this.route.snapshot.paramMap.get('frameworkId')!;

    this.load();
  }

  load() {
    this.boardService.getConfig(this.frameworkId).subscribe(config => {
      this.columns.set(config.columns.sort((a,b) => a.order - b.order));

      this.controlService.getControls(this.frameworkId).subscribe(res => {
        this.controls.set(res);
        this.groupControls();
      });
    });
  }

  groupControls() {
    const groups: Record<string, CompanyControl[]> = {};

    this.columns().forEach(col => {
      groups[col.key] = [];
    });

    this.controls().forEach(control => {
      if (!groups[control.status]) {
        groups[control.status] = [];
      }
      groups[control.status].push(control);
    });

    this.grouped.set(groups);
  }

  drop(event: CdkDragDrop<CompanyControl[]>, newStatus: string) {
    const control = event.previousContainer.data[event.previousIndex];

    this.controlService.updateStatus(control.id, newStatus).subscribe(() => {
      control.status = newStatus;
      this.groupControls();
    });
  }

  changeStatus(control: CompanyControl, status: string) {
    this.controlService.updateStatus(control.id, status).subscribe(() => {
      control.status = status;
      this.groupControls();
    });
  }
}