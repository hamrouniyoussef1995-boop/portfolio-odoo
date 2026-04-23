from odoo import _, api, fields, models
import requests


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def action_generate_ai_description(self):

        api_key = self.env['ir.config_parameter'].sudo().get_param('openai_api_key')

        for product in self:
            category = product.categ_id.name if product.categ_id else "Uncategorized"
            prompt = f"""
            Write a professional product description.
            Product name: {product.name}
            Category: {category}
            Requirements:
            - short and clear
            - marketing tone
            - professional style
            """
            try:
                response = requests.post(
                    "https://api.openai.com/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json",
                    },
                    json={
                        "model": "gpt-4o-mini",
                        "messages": [
                            {"role": "user", "content": prompt}
                        ],
                    },
                )

                result = response.json()

                description = result["choices"][0]["message"]["content"]
                product.description_sale = description

            except Exception as e:
                product.description_sale = "generation desc is failed "
