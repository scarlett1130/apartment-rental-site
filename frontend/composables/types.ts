export interface Apartment {
    id: number;
    rooms?: number;
    name: string;
    location: ApartmentLocation;
    price: number;
    bathrooms: number;
    description: string;
    apartment_image: ApartmentImage[];
    apartment_type?: ApartmentType;
    furnishing?: boolean;
    kitchen?: boolean
    garage?: boolean
    features: ApartmentFeature[];
    apartment_contact?: ApartmentContact;
    available_from?: Date
    available_to?: Date;
    available_to_undefined: boolean
}

export interface ApartmentLocation {
    id: number;
    city: string;
    long: number;
    lat: number;
    address?: string;
}

export interface ApartmentType {
    id: number;
    name: string;
    image: string;
}

export interface ApartmentImage {
    id: number;
    image: string;
}

export interface ApartmentFeature {
    id: number;
    name: string;
}

export interface ApartmentContact {
    id: number
    email: string
    phone: string
}
