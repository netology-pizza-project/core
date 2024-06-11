export interface IPizzaCart {
	product_id: string;
	product_image: string;
	product_title: string;
	product_price: number;
	count?: number;
	product_description?: string;
	product_is_new?: boolean;
	product_is_available?: boolean;
}
