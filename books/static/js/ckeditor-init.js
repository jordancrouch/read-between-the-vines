/**
 *  * This configuration was generated using the CKEditor 5 Builder. You can modify it anytime using this link:
 *   * https://ckeditor.com/ckeditor-5/builder/#installation/NoNgNARATAdCMEYKQOwqgThFbG8FYBmfAFhJQAZ8UQSNyKUSEEiAOCj5CAUwDtkFMMARghQ0RIC6kACZsePQhgDGEKUA
 *    */

const {
  ClassicEditor,
  Autoformat,
  Autosave,
  BlockQuote,
  Bold,
  Essentials,
  Heading,
  Indent,
  IndentBlock,
  Italic,
  Link,
  List,
  ListProperties,
  MediaEmbed,
  Paragraph,
  PasteFromOffice,
  Table,
  TableCaption,
  TableCellProperties,
  TableColumnResize,
  TableProperties,
  TableToolbar,
  TextTransformation,
  TodoList,
  Underline,
} = window.CKEDITOR;

const LICENSE_KEY =
  "eyJhbGciOiJFUzI1NiJ9.eyJleHAiOjE3NTA2MzY3OTksImp0aSI6IjhmMmM5NWM4LTM4MGUtNDE3Ni1hY2FjLWZjNzM1MmNjZjhlYiIsInVzYWdlRW5kcG9pbnQiOiJodHRwczovL3Byb3h5LWV2ZW50LmNrZWRpdG9yLmNvbSIsImRpc3RyaWJ1dGlvbkNoYW5uZWwiOlsiY2xvdWQiLCJkcnVwYWwiLCJzaCJdLCJ3aGl0ZUxhYmVsIjp0cnVlLCJsaWNlbnNlVHlwZSI6InRyaWFsIiwiZmVhdHVyZXMiOlsiKiJdLCJ2YyI6IjcyYjA5YTk3In0.ahLaNMUuLEFScQdAktHnth64xN_EsazMGLT3FdwoBeBrvAx2d-oBc56LTP5Iyqj5AmI0XdjUff0b8Fx5itrC9w";

const editorConfig = {
  toolbar: {
    items: [
      "undo",
      "redo",
      "|",
      "heading",
      "|",
      "bold",
      "italic",
      "underline",
      "|",
      "link",
      "mediaEmbed",
      "insertTable",
      "blockQuote",
      "|",
      "bulletedList",
      "numberedList",
      "todoList",
      "outdent",
      "indent",
    ],
    shouldNotGroupWhenFull: false,
  },
  plugins: [
    Autoformat,
    Autosave,
    BlockQuote,
    Bold,
    Essentials,
    Heading,
    Indent,
    IndentBlock,
    Italic,
    Link,
    List,
    ListProperties,
    MediaEmbed,
    Paragraph,
    PasteFromOffice,
    Table,
    TableCaption,
    TableCellProperties,
    TableColumnResize,
    TableProperties,
    TableToolbar,
    TextTransformation,
    TodoList,
    Underline,
  ],
  heading: {
    options: [
      {
        model: "paragraph",
        title: "Paragraph",
        class: "ck-heading_paragraph",
      },
      {
        model: "heading1",
        view: "h1",
        title: "Heading 1",
        class: "ck-heading_heading1",
      },
      {
        model: "heading2",
        view: "h2",
        title: "Heading 2",
        class: "ck-heading_heading2",
      },
      {
        model: "heading3",
        view: "h3",
        title: "Heading 3",
        class: "ck-heading_heading3",
      },
      {
        model: "heading4",
        view: "h4",
        title: "Heading 4",
        class: "ck-heading_heading4",
      },
      {
        model: "heading5",
        view: "h5",
        title: "Heading 5",
        class: "ck-heading_heading5",
      },
      {
        model: "heading6",
        view: "h6",
        title: "Heading 6",
        class: "ck-heading_heading6",
      },
    ],
  },
  initialData: "<p>Content goes here...</p>",
  licenseKey: LICENSE_KEY,
  link: {
    addTargetToExternalLinks: true,
    defaultProtocol: "https://",
    decorators: {
      toggleDownloadable: {
        mode: "manual",
        label: "Downloadable",
        attributes: {
          download: "file",
        },
      },
    },
  },
  list: {
    properties: {
      styles: true,
      startIndex: true,
      reversed: true,
    },
  },
  placeholder: "Type or paste your content here!",
  table: {
    contentToolbar: [
      "tableColumn",
      "tableRow",
      "mergeTableCells",
      "tableProperties",
      "tableCellProperties",
    ],
  },
};

document.addEventListener("DOMContentLoaded", () => {
  const contentEl = document.getElementById("ckeditor-content");
  if (contentEl) {
    ClassicEditor.create(contentEl, editorConfig).catch((error) => {
      console.error("CKEditor init error:", error);
    });
  }
});
