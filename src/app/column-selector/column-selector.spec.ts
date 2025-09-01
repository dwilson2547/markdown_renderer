import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ColumnSelector } from './column-selector';

describe('ColumnSelector', () => {
  let component: ColumnSelector;
  let fixture: ComponentFixture<ColumnSelector>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ColumnSelector]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ColumnSelector);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
