import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DocRender } from './doc-render';

describe('DocRender', () => {
  let component: DocRender;
  let fixture: ComponentFixture<DocRender>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DocRender]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DocRender);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
