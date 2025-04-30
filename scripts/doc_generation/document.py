"""Base document module for rendering templates with Jinja2 and exporting with WeasyPrint."""

from abc import ABC, abstractmethod
from pathlib import Path

from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader, Template

from settings import TEMPLATES_DIR, EXPORT_DIR


class Document(ABC):
    """Abstract base class for generating documents from templates."""

    template: str = None
    export_path: Path = EXPORT_DIR
    export_name: str = "document"
    jinja_env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

    @property
    def html(self) -> str:
        """Render and cache the HTML content from the Jinja2 template."""
        if not hasattr(self, "_html"):
            setattr(self, "_html", self.render_template())
        return getattr(self, "_html")

    @abstractmethod
    def get_context(self) -> dict:
        """Return the context dictionary for rendering the template."""

    def get_template(self) -> Template:
        """Load and return the template specified by the class."""
        if self.template is None:
            raise ValueError("Template not specified.")
        return self.jinja_env.get_template(self.template)

    def render_template(self) -> str:
        """Render the Jinja2 template using the provided context."""
        return self.get_template().render(self.get_context())

    @property
    def html_path(self) -> Path:
        """Get the full path for the exported HTML file."""
        return self.export_path / (self.export_name + ".html")

    def save_as_html(self) -> None:
        """Save the rendered HTML content to a .html file in the export directory."""
        with open(self.html_path, "w", encoding="utf-8") as html_file:
            html_file.write(self.html)

    @property
    def pdf_path(self) -> Path:
        """Get the full path for the exported PDF file."""
        return self.export_path / (self.export_name + ".pdf")

    def save_as_pdf(self) -> None:
        """Convert the rendered HTML to a PDF and save it to the export directory."""
        HTML(string=self.html).write_pdf(self.pdf_path)
